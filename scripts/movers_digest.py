#!/usr/bin/env python3
"""Generate weekly Movers & Shakers digest from data/catalog.json."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def build_digest(catalog: dict) -> str:
    stats = catalog.get("stats", {})
    entries = catalog.get("entries", [])
    generated_at = catalog.get("generated_at", "")

    movers = [
        e for e in entries
        if isinstance((e.get("github") or {}).get("stars_delta"), int)
        and e["github"]["stars_delta"] > 0
    ]
    movers.sort(key=lambda e: e["github"]["stars_delta"], reverse=True)

    new_entries = [e for e in entries if e.get("is_new")]
    archived = [e for e in entries if (e.get("github") or {}).get("archived")]
    errors = [e for e in entries if (e.get("github") or {}).get("error")]

    top_starred = [
        e for e in entries
        if isinstance((e.get("github") or {}).get("stars"), int)
    ]
    top_starred.sort(key=lambda e: e["github"]["stars"], reverse=True)

    lines: list[str] = [
        "# Awesome AECO — Weekly Movers & Shakers",
        "",
        f"*Generated: `{generated_at}` · Entries: **{stats.get('total_entries', len(entries))}** · "
        f"GitHub Repos: **{stats.get('github_repos', 0)}** · Categories: **{stats.get('categories', 0)}***",
        "",
    ]

    if movers:
        lines.extend(["## Fastest-Growing Repositories", ""])
        for rank, item in enumerate(movers[:10], start=1):
            gh = item["github"]
            delta = gh["stars_delta"]
            stars = gh["stars"]
            lang = gh.get("language") or "—"
            lic = gh.get("license") or "—"
            lines.append(
                f"{rank}. **[{item['name']}]({item['github_url']})** (`+{delta:,}` stars → `{stars:,}` total) — "
                f"*{item['category']}* · {lang} · {lic}"
            )
            lines.append(f"   {item['description']}")
        lines.append("")
    else:
        lines.extend([
            "## Baseline Snapshot — Top Starred Repositories",
            "",
            "*Star-velocity deltas will appear automatically on the next weekly run.*",
            "",
        ])
        for rank, item in enumerate(top_starred[:10], start=1):
            gh = item["github"]
            stars = gh["stars"]
            lang = gh.get("language") or "—"
            lic = gh.get("license") or "—"
            lines.append(
                f"{rank}. **[{item['name']}]({item['github_url']})** (`{stars:,}` stars) — "
                f"*{item['category']}* · {lang} · {lic}"
            )
        lines.append("")

    if new_entries:
        lines.extend(["## Newly Added Entries", ""])
        for item in new_entries:
            link = item.get("github_url") or item.get("website") or ""
            lines.append(f"- **[{item['name']}]({link})** (*{item['category']}*): {item['description']}")
        lines.append("")

    if archived:
        lines.extend(["## Archived Repositories (Review Needed)", ""])
        for item in archived:
            lines.append(f"- **[{item['name']}]({item['github_url']})** (*{item['category']}*) — marked archived on GitHub")
        lines.append("")

    if errors:
        lines.extend(["## GitHub API Fetch Errors", ""])
        for item in errors:
            err = item["github"]["error"]
            lines.append(f"- **[{item['name']}]({item['github_url']})** (`{item['github_repo']}`): `{err}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Movers & Shakers digest from data/catalog.json")
    parser.add_argument("--catalog", type=Path, default=Path("data/catalog.json"))
    parser.add_argument("--output", type=Path, default=Path("data/movers.md"))
    args = parser.parse_args()

    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    md = build_digest(catalog)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(md, encoding="utf-8")
    print(f"Wrote {args.output}")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write("\n" + md)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
