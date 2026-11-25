#!/usr/bin/env python3
"""Generate a PR badge comment and social/newsletter drafts for newly merged readme.md entries."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Any

from build_catalog import fetch_github_repo, parse_readme

BADGE_URL = "https://raw.githubusercontent.com/awesome-aeco/Awesome-AECO/main/badges/featured-in-awesome-aeco.svg"
REPO_URL = "https://github.com/awesome-aeco/Awesome-AECO"


def load_entries_from_git_ref(ref: str, readme_rel: str = "readme.md") -> list[dict[str, Any]]:
    content = subprocess.check_output(["git", "show", f"{ref}:{readme_rel}"], text=True)
    tmp = Path("/tmp/_awesome_aeco_ref_readme.md")
    tmp.write_text(content, encoding="utf-8")
    try:
        return parse_readme(tmp)
    finally:
        tmp.unlink(missing_ok=True)


def build_badge_comment(new_entries: list[dict[str, Any]]) -> str:
    names = ", ".join(f"**{e['name']}**" for e in new_entries)
    return (
        f"Thank you for contributing {names} to **Awesome AECO**!\n\n"
        "If you maintain this project, you're welcome to add the **Featured in Awesome AECO** badge to your README:\n\n"
        "**Markdown**\n"
        "```markdown\n"
        f"[![Featured in Awesome AECO]({BADGE_URL})]({REPO_URL})\n"
        "```\n\n"
        "**HTML**\n"
        "```html\n"
        f'<a href="{REPO_URL}"><img src="{BADGE_URL}" alt="Featured in Awesome AECO"></a>\n'
        "```\n\n"
        f"See [`brand/README.md`]({REPO_URL}/blob/main/brand/README.md) for logos and usage guidelines.\n"
    )


def build_content_drafts(new_entries: list[dict[str, Any]], token: str | None) -> str:
    sections: list[str] = ["# Awesome AECO — Content Drafts for Merged PR", ""]

    for entry in new_entries:
        gh_data = fetch_github_repo(entry["github_repo"], token) if entry.get("github_repo") else None
        stars = (gh_data or {}).get("stars")
        lang = (gh_data or {}).get("language")
        lic = (gh_data or {}).get("license")

        meta_parts = [p for p in [lang, lic, f"{stars:,} stars" if isinstance(stars, int) else None] if p]
        meta_str = " · ".join(meta_parts) if meta_parts else "Open AECO resource"
        primary_url = entry.get("github_url") or entry.get("website") or REPO_URL
        tags = ", ".join(entry.get("tags") or [entry["category"]])

        sections.extend([
            f"## {entry['name']}",
            f"- **Domain:** `{entry['category']}`",
            f"- **Intent:** `Discovery`",
            f"- **Tags:** `{tags}`",
            f"- **Stats:** {meta_str}",
            f"- **URL:** {primary_url}",
            "",
            "### Open AECO Digest (Newsletter Blurb)",
            f"> **[{entry['name']}]({primary_url})** (*{entry['category']}* · {meta_str}) — {entry['description']}",
            "",
            "### LinkedIn Draft",
            "```text",
            f"New in Awesome AECO ({entry['category']}): {entry['name']}",
            "",
            f"{entry['description']}",
            "",
            f"Stack / Details: {meta_str}",
            f"Explore the project: {primary_url}",
            f"Full curated directory: {REPO_URL}",
            "",
            "#AECO #OpenBIM #AEC #OpenSource",
            "```",
            "",
            "### X / Bluesky Draft",
            "```text",
            f"Added to Awesome AECO ({entry['category']}): {entry['name']}",
            "",
            f"{entry['description']}",
            "",
            f"{primary_url}",
            "```",
            "",
        ])

    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate PR badge comment and content drafts")
    parser.add_argument("--base", default="HEAD~1", help="Base git ref")
    parser.add_argument("--head", default="HEAD", help="Head git ref")
    parser.add_argument("--out-dir", type=Path, default=Path("pr-artifacts"))
    args = parser.parse_args()

    base_entries = load_entries_from_git_ref(args.base)
    head_entries = load_entries_from_git_ref(args.head)

    base_ids = {e["id"] for e in base_entries}
    new_entries = [e for e in head_entries if e["id"] not in base_ids]

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "new_entries.json").write_text(
        json.dumps(new_entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    if not new_entries:
        print("No newly added entries detected in diff.")
        return 0

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    comment_md = build_badge_comment(new_entries)
    drafts_md = build_content_drafts(new_entries, token)

    (args.out_dir / "badge_comment.md").write_text(comment_md, encoding="utf-8")
    (args.out_dir / "content_drafts.md").write_text(drafts_md, encoding="utf-8")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write("\n" + drafts_md)

    print(f"Generated badge comment and content drafts for {len(new_entries)} new entry/entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
