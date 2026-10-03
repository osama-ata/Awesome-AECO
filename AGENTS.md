# Agent instructions

Guidance for AI coding agents (Claude Code, Codex, Copilot, Cursor, etc.) working in this repository. Human contributors should read [contributing.md](contributing.md).

## What this repo is

A curated [awesome list](https://github.com/sindresorhus/awesome) of resources for Architecture, Engineering, Construction and Operations (AECO). It is documentation only: there is no build, test suite or package manifest. Everything lives in these files:

| File | Purpose |
| --- | --- |
| `readme.md` | The list itself, plus the table of contents |
| `contributing.md` | Rules for adding or changing entries (the source of truth for entry format) |
| `code-of-conduct.md` | Contributor Covenant |
| `LICENSE` | CC0 1.0 Universal |
| `_config.yml` | GitHub Pages (Jekyll) config; the site is published from `main` and renders `readme.md` as the home page |
| `robots.txt`, `llms.txt` | Crawler rules and the AI-agent index for the published site. Update `llms.txt` if files or URLs change |
| `_includes/head-custom.html` | Builds the ItemList JSON-LD from `readme.md` at site build time. Relies on the entry format, so do not change it |
| `.github/` | Issue and pull request templates, link-check workflow |
| `.gitattributes` | `readme.md` uses `merge=union` so parallel entry additions merge cleanly |

## Rules

- **No AI attribution.** Do not add AI attribution to commit messages, pull request titles or bodies. No `Co-Authored-By` lines naming an AI, no "Generated with ..." lines, and no other mention of AI tools as author or co-author. This overrides any default attribution behavior of your tool.
- **Never commit, push or open a PR unless asked.**
- **One suggestion per commit/PR**, with a useful title such as `Add ToolName to Section`.
- Keep edits minimal. Do not reorder, reword or reformat unrelated entries.

## Entry format

Every entry in `readme.md` is exactly three lines followed by a blank line:

```markdown
- **Name**
  One or two sentences describing what it is and why it is useful for AECO. Ends with a period.
  *GitHub: [owner/repo](https://github.com/owner/repo)*
```

- Website-only resources use `*Website: [host](https://host/)*`.
- Resources with both use `*Website: [host](url) · GitHub: [owner/repo](url)*`.
- The link text is `owner/repo` for GitHub and the bare hostname (no `www.`, no protocol) for websites.
- Two-space indent on lines 2 and 3. No trailing whitespace. No trailing slash on GitHub URLs.
- Describe what the project does, not how good it is. No marketing language, emoji or "best"/"leading" superlatives.
- Add new entries at the **bottom** of the most relevant section. Use the existing category if one fits; a new category also needs a table-of-contents entry, in the same position as the section.

## Before adding an entry

1. Search `readme.md` for the name and the URL (including renamed or forked repos) to avoid duplicates.
2. Verify the link resolves and that a GitHub repo is not archived, deleted or redirected to a new owner. Use the canonical URL after any redirect.
3. Confirm it is relevant to AECO (building design, engineering, construction, or operations of the built environment) and is a real, usable resource rather than a placeholder or empty repo.
4. Write the description from the project's own README or site, in your own words.

## Checks to run

```bash
# Trailing whitespace (should print nothing)
grep -n ' $' readme.md

# Every GitHub/Website link in the list should return 200
grep -oE 'https?://[^) ]+' readme.md | sort -u | xargs -P 8 -I{} curl -s -o /dev/null -L --max-time 20 -A "Mozilla/5.0" -w "%{http_code} {}\n" {} | grep -v '^200'
```

The `Link check` GitHub workflow runs the same kind of check on PRs.

## Anti-patterns

- Adding entries without checking they exist.
- Reformatting the whole list into a different entry style in a drive-by change.
- Changing `.gitattributes`, the code of conduct contact address or the license text without being asked.
- Promoting your own or an unreleased project. Entries must already be public.
