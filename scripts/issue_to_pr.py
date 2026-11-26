#!/usr/bin/env python3
"""Parse a GitHub 'Suggest a resource' Issue Form and insert a validated entry into readme.md."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from lint_readme import lint_readme

GITHUB_RE = re.compile(r"^https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/?$")
NO_RESPONSE = {"", "_no response_", "none", "n/a", "-"}


def parse_issue_body(body: str) -> dict[str, str]:
    """Parse GitHub Issue Form markdown (`### Heading\\n\\nValue`)."""
    sections: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in body.splitlines():
        if line.startswith("### "):
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = line[4:].strip().lower()
            buf = []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def clean_field(value: str) -> str:
    val = " ".join(value.strip().split())
    return "" if val.lower() in NO_RESPONSE else val


def check_url(url: str) -> tuple[bool, str, str]:
    """Return (ok, canonical_url, error_message)."""
    if not url.startswith(("http://", "https://")):
        return False, url, f"URL must start with http:// or https://: {url}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            if resp.status != 200:
                return False, resp.geturl(), f"HTTP {resp.status} for {url}"
            return True, resp.geturl(), ""
    except urllib.error.HTTPError as exc:
        return False, url, f"HTTP {exc.code} for {url}"
    except Exception as exc:
        return False, url, f"Failed to reach {url}: {exc}"


def check_github_repo(gh_url: str, token: str | None) -> tuple[bool, str, str]:
    """Verify GitHub repo exists, is not archived, and return canonical https://github.com/owner/repo."""
    m = GITHUB_RE.match(gh_url.strip())
    if not m:
        return False, gh_url, f"GitHub URL must look like https://github.com/owner/repo (got: {gh_url})"
    repo = m.group(1)
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return False, gh_url, f"GitHub repo check failed (HTTP {exc.code}) for {repo}"
    except Exception as exc:
        return False, gh_url, f"GitHub API error for {repo}: {exc}"

    if data.get("archived"):
        return False, gh_url, f"GitHub repository `{data.get('full_name', repo)}` is archived."
    canonical = f"https://github.com/{data['full_name']}"
    return True, canonical, ""


def format_entry(name: str, description: str, github_url: str, website_url: str) -> str:
    desc = description.strip()
    if not desc.endswith("."):
        desc += "."

    link_parts: list[str] = []
    if website_url:
        host = urllib.parse.urlparse(website_url).netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        link_parts.append(f"Website: [{host}]({website_url})")
    if github_url:
        repo = GITHUB_RE.match(github_url).group(1)  # type: ignore[union-attr]
        link_parts.append(f"GitHub: [{repo}]({github_url})")

    links_line = f"*{' · '.join(link_parts)}*"
    return f"- **{name}**\n  {desc}\n  {links_line}\n"


def insert_entry(readme_text: str, category: str, entry_md: str) -> tuple[bool, str, str]:
    heading = f"## {category}"
    lines = readme_text.splitlines(keepends=True)
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start_idx = i
            break
    if start_idx is None:
        return False, readme_text, f"Category heading `{heading}` not found in readme.md."

    insert_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            insert_idx = j
            break

    # Ensure single blank line before new entry and single blank line before next heading
    prefix = "".join(lines[:insert_idx]).rstrip("\n") + "\n\n"
    suffix = "".join(lines[insert_idx:]).lstrip("\n")
    updated = prefix + entry_md + ("\n" + suffix if suffix else "")
    return True, updated, ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert a Suggest a resource issue into a readme.md edit")
    parser.add_argument("--body-file", type=Path, required=True)
    parser.add_argument("--readme", type=Path, default=Path("readme.md"))
    parser.add_argument("--meta-out", type=Path, required=True)
    args = parser.parse_args()

    body = args.body_file.read_text(encoding="utf-8")
    fields = parse_issue_body(body)

    name = clean_field(fields.get("project name", ""))
    github_url = clean_field(fields.get("github repository url", ""))
    website_url = clean_field(fields.get("website url", ""))
    category = clean_field(fields.get("category", ""))
    description = clean_field(fields.get("description", ""))
    is_author = clean_field(fields.get("are you the author or a maintainer of this project?", ""))

    errors: list[str] = []
    if not name:
        errors.append("Missing required field: **Project name**.")
    if not category:
        errors.append("Missing required field: **Category**.")
    if not description:
        errors.append("Missing required field: **Description**.")
    if not github_url and not website_url:
        errors.append("Provide at least one of **GitHub repository URL** or **Website URL**.")

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if github_url:
        ok, github_url, err = check_github_repo(github_url, token)
        if not ok:
            errors.append(err)
    if website_url:
        ok, website_url, err = check_url(website_url)
        if not ok:
            errors.append(err)

    readme_text = args.readme.read_text(encoding="utf-8")
    readme_lower = readme_text.lower()
    if github_url and github_url.lower() in readme_lower:
        errors.append(f"`{github_url}` is already listed in `readme.md`.")
    if website_url and website_url.rstrip("/").lower() in readme_lower:
        errors.append(f"`{website_url}` appears to already be listed in `readme.md`.")
    if name and f"- **{name.lower()}**" in readme_lower:
        errors.append(f"An entry named **{name}** is already listed in `readme.md`.")

    if errors:
        args.meta_out.write_text(json.dumps({"ok": False, "errors": errors}, indent=2) + "\n", encoding="utf-8")
        return 0

    entry_md = format_entry(name, description, github_url, website_url)
    ok, updated_readme, err = insert_entry(readme_text, category, entry_md)
    if not ok:
        args.meta_out.write_text(json.dumps({"ok": False, "errors": [err]}, indent=2) + "\n", encoding="utf-8")
        return 0

    args.readme.write_text(updated_readme, encoding="utf-8")
    lint_errors = lint_readme(args.readme)
    if lint_errors:
        args.readme.write_text(readme_text, encoding="utf-8")
        args.meta_out.write_text(
            json.dumps({"ok": False, "errors": [f"Lint check failed: {e}" for e in lint_errors]}, indent=2) + "\n",
            encoding="utf-8",
        )
        return 0

    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:40] or "resource"
    args.meta_out.write_text(
        json.dumps(
            {
                "ok": True,
                "name": name,
                "category": category,
                "github_url": github_url,
                "website_url": website_url,
                "is_author": is_author,
                "slug": slug,
                "pr_title": f"Add {name} to {category}",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
