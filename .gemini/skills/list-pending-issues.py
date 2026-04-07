# .gemini/skills/list-pending-issues.py
"""
An agent skill to list all pending (non‑archived) issue Markdown files
ordered by project name and numeric issue ID.

Usage (from repository root):

    python .gemini/skills/list-pending-issues.py

The script outputs a sorted list of file paths.
"""

import sys
from pathlib import Path
import re

# Configuration
ROOT = Path("issues")
ARCHIVE = "archive"
ISSUE_PATTERN = re.compile(r"ISSUE-([0-9]+)-.*\.md$")


def main():
    issues = []
    for path in ROOT.rglob("ISSUE-*.md"):
        if ARCHIVE in path.parts:
            continue
        match = ISSUE_PATTERN.search(path.name)
        if not match:
            continue
        issue_id = int(match.group(1))
        project = path.parts[0]  # 'issues'
        # actual project name is second part
        project = path.parts[1]
        issues.append((project, issue_id, path.relative_to(ROOT)))
    # Sort by project, then numeric id
    issues.sort(key=lambda x: (x[0], x[1]))
    for proj, i, rel in issues:
        print(f"{proj} - ISSUE-{i:03d}: {rel}")


if __name__ == "__main__":
    main()
