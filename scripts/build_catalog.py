#!/usr/bin/env python3
"""Parse readme.md and enrich entries with GitHub metadata into data/catalog.json."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

NON_CATEGORY_SECTIONS = {
    "Contents",
    "FAQ",
    "Related Lists",
    "Contribute",
    "License",
}

ENTRY_TITLE_RE = re.compile(r"^- \*\*(.+?)\*\*$")
GITHUB_RE = re.compile(r"GitHub: \[([^\]]+)\]\((https://github\.com/[^)\s]+)\)")
WEBSITE_RE = re.compile(r"Website: \[([^\]]+)\]\((https?://[^)\s]+)\)")
REPO_SLUG_RE = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+)$")

TAG_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("IFC", re.compile(r"\bifc(?:2x3|4|4x3)?\b", re.I)),
    ("ISO 19650", re.compile(r"\biso[\s-]?19650\b", re.I)),
    ("IDS", re.compile(r"\bids\b", re.I)),
    ("BCF", re.compile(r"\bbcf\b", re.I)),
    ("CityGML", re.compile(r"\bcitygml\b", re.I)),
    ("CityJSON", re.compile(r"\bcityjson\b", re.I)),
    ("MCP", re.compile(r"\bmcp\b|model context protocol", re.I)),
    ("Revit", re.compile(r"\brevit\b", re.I)),
    ("Blender", re.compile(r"\bblender\b|bonsai", re.I)),
    ("Grasshopper", re.compile(r"\bgrasshopper\b", re.I)),
    ("Rhino", re.compile(r"\brhino(?:3d)?\b", re.I)),
    ("FreeCAD", re.compile(r"\bfreecad\b", re.I)),
    ("DWG/DXF", re.compile(r"\b(?:dwg|dxf)\b", re.I)),
    ("Point Cloud", re.compile(r"point cloud|lidar|las/laz|photogrammetry", re.I)),
    ("FEA/Structural", re.compile(r"\bfea\b|finite element|structural|seismic", re.I)),
    ("Energy", re.compile(r"energyplus|openstudio|thermal|daylight|hvac|building energy", re.I)),
    ("WebGPU", re.compile(r"\bwebgpu\b", re.I)),
    ("WASM", re.compile(r"\bwasm\b|webassembly", re.I)),
    ("AI/LLM", re.compile(r"\b(?:ai|llm|agent|rag)\b", re.I)),
    ("GIS", re.compile(r"\bgis\b|geospatial|qgis|gdal", re.I)),
    ("Cost/BOQ", re.compile(r"\bboq\b|takeoff|estimat|cost", re.I)),
]


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug


def infer_tags(name: str, category: str, description: str, topics: list[str] | None = None) -> list[str]:
    haystack = f"{name} {category} {description}"
    tags: list[str] = []
    for tag, pattern in TAG_PATTERNS:
        if pattern.search(haystack):
            tags.append(tag)
    if topics:
        for t in topics[:6]:
            if t.lower() in {"ifc", "bim", "openbim", "cad", "gis", "revit", "freecad", "blender", "mcp"}:
                label = t.upper() if len(t) <= 3 else t
                if label not in tags and label.lower() not in {x.lower() for x in tags}:
                    tags.append(label)
    return tags


def parse_readme(readme_path: Path) -> list[dict[str, Any]]:
    lines = readme_path.read_text(encoding="utf-8").splitlines()
    entries: list[dict[str, Any]] = []
    current_section: str | None = None

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            current_section = line[3:].strip()
            i += 1
            continue

        if current_section is None or current_section in NON_CATEGORY_SECTIONS:
            i += 1
            continue

        title_match = ENTRY_TITLE_RE.match(line)
        if title_match and i + 2 < len(lines):
            name = title_match.group(1).strip()
            description = lines[i + 1].strip()
            link_line = lines[i + 2].strip()

            gh_match = GITHUB_RE.search(link_line)
            web_match = WEBSITE_RE.search(link_line)

            github_url = gh_match.group(2) if gh_match else None
            website_url = web_match.group(2) if web_match else None

            github_repo = None
            if github_url:
                slug_match = REPO_SLUG_RE.match(github_url.rstrip("/"))
                if slug_match:
                    github_repo = f"{slug_match.group(1)}/{slug_match.group(2)}"

            entries.append(
                {
                    "id": slugify(name),
                    "name": name,
                    "category": current_section,
                    "description": description,
                    "website": website_url,
                    "github_url": github_url,
                    "github_repo": github_repo,
                    "tags": infer_tags(name, current_section, description),
                    "github": None,
                }
            )
            i += 3
            continue

        i += 1

    return entries


def fetch_github_repo(repo: str, token: str | None) -> dict[str, Any] | None:
    url = f"https://api.github.com/repos/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-aeco-catalog-builder",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            license_info = data.get("license") or {}
            return {
                "full_name": data.get("full_name"),
                "stars": data.get("stargazers_count", 0),
                "forks": data.get("forks_count", 0),
                "open_issues": data.get("open_issues_count", 0),
                "language": data.get("language"),
                "license": license_info.get("spdx_id") if license_info.get("spdx_id") != "NOASSERTION" else None,
                "topics": data.get("topics", []),
                "archived": bool(data.get("archived", False)),
                "pushed_at": data.get("pushed_at"),
                "default_branch": data.get("default_branch"),
                "homepage": data.get("homepage") or None,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        return {"error": f"HTTP {exc.code}"}
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


def load_previous_catalog(output_path: Path) -> dict[str, dict[str, Any]]:
    if not output_path.exists():
        return {}
    try:
        data = json.loads(output_path.read_text(encoding="utf-8"))
        return {item["id"]: item for item in data.get("entries", []) if "id" in item}
    except Exception:  # noqa: BLE001
        return {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Build enriched data/catalog.json from readme.md")
    parser.add_argument("--readme", type=Path, default=Path("readme.md"))
    parser.add_argument("--output", type=Path, default=Path("data/catalog.json"))
    parser.add_argument("--skip-github", action="store_true", help="Skip GitHub API enrichment")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent GitHub API workers")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    previous = load_previous_catalog(args.output)
    entries = parse_readme(args.readme)

    enriched_count = 0
    error_count = 0

    def enrich_entry(entry: dict[str, Any]) -> tuple[bool, bool]:
        prev = previous.get(entry["id"])
        prev_gh = (prev or {}).get("github") or {}
        prev_stars = prev_gh.get("stars")

        if args.skip_github or not entry["github_repo"]:
            if prev_gh and not args.skip_github:
                entry["github"] = prev_gh
            return (False, False)

        gh_data = fetch_github_repo(entry["github_repo"], token)
        if gh_data and not gh_data.get("error"):
            stars = gh_data["stars"]
            gh_data["stars_prev"] = prev_stars
            gh_data["stars_delta"] = (stars - prev_stars) if isinstance(prev_stars, int) else None
            entry["github"] = gh_data
            entry["tags"] = infer_tags(
                entry["name"],
                entry["category"],
                entry["description"],
                gh_data.get("topics"),
            )
            return (True, False)

        merged = dict(prev_gh) if prev_gh else {}
        merged["error"] = (gh_data or {}).get("error", "Unknown error")
        entry["github"] = merged
        return (False, True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        for was_enriched, had_error in pool.map(enrich_entry, entries):
            if was_enriched:
                enriched_count += 1
            if had_error:
                error_count += 1

    # Mark newly added entries relative to previous snapshot
    prev_ids = set(previous.keys())
    for entry in entries:
        entry["is_new"] = bool(prev_ids) and (entry["id"] not in prev_ids)

    categories: list[str] = []
    for entry in entries:
        if entry["category"] not in categories:
            categories.append(entry["category"])

    catalog = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "https://github.com/awesome-aeco/Awesome-AECO/blob/main/readme.md",
        "license": "CC-BY-4.0",
        "stats": {
            "total_entries": len(entries),
            "categories": len(categories),
            "github_repos": sum(1 for e in entries if e["github_repo"]),
            "enriched_repos": enriched_count,
            "archived_repos": sum(1 for e in entries if (e.get("github") or {}).get("archived")),
            "fetch_errors": error_count,
        },
        "categories": categories,
        "entries": entries,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"Wrote {args.output}: {len(entries)} entries across {len(categories)} categories "
        f"(enriched={enriched_count}, archived={catalog['stats']['archived_repos']}, errors={error_count})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
