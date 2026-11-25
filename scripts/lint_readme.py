#!/usr/bin/env python3
"""Validate readme.md entry format, TOC sync, duplicates, and whitespace."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NON_CATEGORY_SECTIONS = {
    "Contents",
    "FAQ",
    "Related Lists",
    "Contribute",
    "License",
}

ENTRY_TITLE_RE = re.compile(r"^- \*\*(.+?)\*\*$")
GITHUB_LINK_PART = r"GitHub: \[[^\]]+\]\((https://github\.com/[^)\s]+)\)"
WEBSITE_LINK_PART = r"Website: \[[^\]]+\]\((https?://[^)\s]+)\)"
LINK_LINE_RE = re.compile(
    rf"^  \*(?:{GITHUB_LINK_PART}|{WEBSITE_LINK_PART}|{WEBSITE_LINK_PART} · {GITHUB_LINK_PART})\*$"
)
TOC_ITEM_RE = re.compile(r"^\s*- \[([^\]]+)\]\(#([^)]+)\)$")


def github_slug(heading: str) -> str:
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r" ", "-", slug)
    return slug


def normalize_url(url: str) -> str:
    return url.strip().rstrip("/").lower()


def lint_readme(path: Path) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    # 1. Trailing whitespace check
    for idx, line in enumerate(lines, start=1):
        if line.endswith(" ") or line.endswith("\t"):
            errors.append(f"Line {idx}: trailing whitespace")

    # 2. Collect H2 headings and TOC items
    h2_headings: list[tuple[int, str]] = []
    toc_items: list[tuple[int, str, str]] = []
    in_toc = False

    for idx, line in enumerate(lines, start=1):
        if line.startswith("## "):
            heading = line[3:].strip()
            h2_headings.append((idx, heading))
            in_toc = heading == "Contents"
            continue
        if in_toc:
            if line.strip() == "---":
                in_toc = False
                continue
            match = TOC_ITEM_RE.match(line)
            if match:
                label = match.group(1).replace(r"\&", "&")
                anchor = match.group(2)
                if label != "Awesome AECO":
                    toc_items.append((idx, label, anchor))

    expected_toc = [(h, github_slug(h)) for _, h in h2_headings]
    actual_toc = [(label, anchor) for _, label, anchor in toc_items]
    if actual_toc != expected_toc:
        expected_set = set(expected_toc)
        actual_set = set(actual_toc)
        for label, anchor in expected_toc:
            if (label, anchor) not in actual_set:
                errors.append(f"TOC missing or mismatched heading: '{label}' (#{anchor})")
        for idx, label, anchor in toc_items:
            if (label, anchor) not in expected_set:
                errors.append(f"Line {idx}: TOC entry does not match any ## heading: '{label}' (#{anchor})")
        if expected_set == actual_set:
            errors.append("TOC order does not match section heading order in readme.md")

    # 3. Validate entries in every category section
    seen_names: dict[str, int] = {}
    seen_urls: dict[str, tuple[int, str]] = {}

    i = 0
    current_section: str | None = None
    while i < len(lines):
        line = lines[i]
        line_no = i + 1

        if line.startswith("## "):
            current_section = line[3:].strip()
            i += 1
            continue

        if current_section is None or current_section in NON_CATEGORY_SECTIONS:
            i += 1
            continue

        if line.strip() == "":
            i += 1
            continue

        if line.startswith("- "):
            title_match = ENTRY_TITLE_RE.match(line)
            if not title_match:
                errors.append(
                    f"Line {line_no} [{current_section}]: entry line 1 must match '- **Name**': {line!r}"
                )
                i += 1
                continue

            name = title_match.group(1).strip()
            name_key = name.lower()
            if name_key in seen_names:
                errors.append(
                    f"Line {line_no}: duplicate entry name '{name}' (first seen on line {seen_names[name_key]})"
                )
            else:
                seen_names[name_key] = line_no

            # Line 2: Description
            if i + 1 >= len(lines):
                errors.append(f"Line {line_no}: entry '{name}' is missing description line")
                break
            desc_line = lines[i + 1]
            if not desc_line.startswith("  ") or desc_line.startswith("   ") or desc_line.strip() == "":
                errors.append(
                    f"Line {line_no + 1}: description for '{name}' must be indented by exactly two spaces"
                )
            elif not re.search(r'\.["\')]*$', desc_line.strip()):
                errors.append(
                    f"Line {line_no + 1}: description for '{name}' must end with a period"
                )

            # Line 3: Link line
            if i + 2 >= len(lines):
                errors.append(f"Line {line_no}: entry '{name}' is missing link line")
                break
            link_line = lines[i + 2]
            link_match = LINK_LINE_RE.match(link_line)
            if not link_match:
                errors.append(
                    f"Line {line_no + 2}: link line for '{name}' does not match format "
                    f"'  *GitHub: ...*' or '  *Website: ...*': {link_line!r}"
                )
            else:
                urls = [u for u in link_match.groups() if u]
                for url in urls:
                    if url.startswith("https://github.com/") and url.endswith("/"):
                        errors.append(
                            f"Line {line_no + 2}: GitHub URL for '{name}' must not have a trailing slash: {url}"
                        )
                    norm = normalize_url(url)
                    if norm in seen_urls:
                        prev_line, prev_name = seen_urls[norm]
                        errors.append(
                            f"Line {line_no + 2}: duplicate URL '{url}' for '{name}' "
                            f"(already used by '{prev_name}' on line {prev_line})"
                        )
                    else:
                        seen_urls[norm] = (line_no + 2, name)

            # Line 4: Blank line separator (unless EOF)
            if i + 3 < len(lines) and lines[i + 3].strip() != "":
                errors.append(
                    f"Line {line_no + 3}: expected blank line after entry '{name}'"
                )

            i += 3
            continue

        # Unexpected non-empty line inside a category section
        errors.append(
            f"Line {line_no} [{current_section}]: unexpected line outside 3-line entry format: {line!r}"
        )
        i += 1

    return errors


def main() -> int:
    readme_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("readme.md")
    if not readme_path.exists():
        print(f"Error: {readme_path} not found", file=sys.stderr)
        return 1

    errors = lint_readme(readme_path)
    if errors:
        print(f"Found {len(errors)} lint error(s) in {readme_path}:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: {readme_path} passed all format, TOC, whitespace, and duplicate checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
