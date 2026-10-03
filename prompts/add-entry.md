# Prompt template: add your repo with an AI agent

Copy the prompt below into your AI agent (Claude Code, Codex, Copilot, Cursor, etc.), replace the placeholders in the first block, and let it prepare the pull request. Review the result before you submit it: you are responsible for the accuracy of the entry.

The agent needs shell access and, for opening the pull request, the [GitHub CLI](https://cli.github.com/) (`gh`) signed in to your account.

---

````text
Add a resource to the Awesome AECO list (https://github.com/osama-ata/Awesome-AECO).

Resource to add
- Name: <project name, as the project writes it>
- GitHub: <https://github.com/owner/repo, or leave empty>
- Website: <https://example.com, or leave empty>
- Suggested section: <e.g. "BIM & IFC", or leave empty to let the agent choose>
- I am the author or a maintainer of this project: <yes / no>

Steps
1. Fork and clone https://github.com/osama-ata/Awesome-AECO, then create a branch named add-<project-name>.
2. Read AGENTS.md and contributing.md in the clone. They are the source of truth for the entry format and the checks. Follow them exactly.
3. Check for duplicates: search readme.md for the project name, the repo URL and any former or forked names. If the project is already listed, stop and tell me.
4. Verify the resource:
   - The links resolve with HTTP 200. Use the canonical URL after any redirect.
   - A GitHub repo is not archived, deleted, empty or redirected to a new owner.
   - It is relevant to AECO (design, engineering, construction or operation of buildings and infrastructure) and is a real, usable project.
   If any check fails, stop and tell me why instead of adding it.
5. Read the project's own README or site and write the description in your own words: one or two sentences, factual, ending with a period. Say what it does and why it helps in AECO. No marketing language, emoji or words like "best" or "leading".
6. Pick the most relevant existing section of readme.md (my suggestion above if it fits) and add the entry at the bottom of that section, in exactly this format with a blank line after it:

   - **Name**
     Description.
     *GitHub: [owner/repo](https://github.com/owner/repo)*

   Use `*Website: [host](https://host/)*` for website-only resources, and `*Website: [host](url) · GitHub: [owner/repo](url)*` when there are both. Link text is owner/repo for GitHub and the bare hostname (no www., no protocol) for websites. Two-space indent on lines 2 and 3, no trailing whitespace, no trailing slash on GitHub URLs.
7. Change nothing else: do not reorder, reword or reformat other entries, and do not touch other files.
8. Run the checks from AGENTS.md (trailing whitespace and link check) and show me the output.
9. Show me the diff and wait for my approval before committing.
10. After I approve, commit with the title "Add <Name> to <Section>" and open a pull request against osama-ata/Awesome-AECO with the same title. In the pull request description, say whether I am the author or a maintainer, and give the link to the project.

Rules
- Do not add AI attribution anywhere: no Co-Authored-By lines naming an AI, no "Generated with ..." lines, and no mention of AI tools in the commit message or pull request.
- One resource per pull request.
- Do not invent facts about the project. If the README does not support a claim, leave it out.
````
