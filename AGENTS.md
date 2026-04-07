# AGENTS.md

This document defines the conventions and tooling expectations for agents operating in this repository. It incorporates the *GEMINI Mandates* that govern issue tracking, and provides the build, lint, and test commands.

## 1. Issue Tracking (GEMINI Mandates)

### 1.1 Directory Structure
- **Root**: `issues/`
- **Project Folder**: `issues/[project-name]/`
- **Template**: `issues/ISSUE_TEMPLATE.md`
- **Knowledge Base**: `issues/[project-name]/kb/`
- **Archive**: `issues/[project-name]/archive/`

### 1.2 Naming Convention
- **Issue**: `ISSUE-<ID>-<short‑kebab‑case-description>.md` (e.g., `ISSUE-001-boot-hang.md`)
- **Archive Issue**: prepend `CLOSED-` to the original filename (`CLOSED-ISSUE-001-boot-hang.md`).
- **KB Article**: `KB-<ID>-<short‑kebab‑case-description>.md` (e.g., `KB-001-common-boot-issues.md`).

### 1.3 Professional Rewriting Standards
- **Tone**: Technical, precise, objective.
- **Structure**: Always follow the `ISSUE_TEMPLATE.md` / `KB_TEMPLATE.md` layout.
- **Focus**: Impact, root causes (race conditions, synchronization, hardware issues), acceptance criteria, diagnostic strategies (marked *Optional* when unconfirmed).

### 1.4 Operational Workflow
1. **Create project directory** if missing: `mkdir -p issues/[project-name]`.
2. **Write / Replace** files using the provided APIs (`write_file`, `replace`).
3. **Archiving**: When an issue contains `Status: Closed`, move it to `archive/` and rename with the `CLOSED-` prefix.
4. **KB Articles**: Create or update in `issues/[project-name]/kb/` following the same rewrite standards.

---

**File Organization (for reference)**
```
/home/zzlee/docker/issue-tracker/
├── AGENTS.md
├── GEMINI.md
├── README.md
├── pyproject.toml
├── main.py
├── issues/
│   ├── ISSUE_TEMPLATE.md
│   ├── KB_TEMPLATE.md
│   └── [project-name]/
│       ├── ISSUE-*.md
│       ├── kb/KB-*.md
│       └── archive/
└── .gemini/
    └── skills/
```

## 3. OpenCode Skills

### 3.1 List Pending Issues
- **Script**: `.gemini/skills/list-pending-issues.py`
- **Command**: `uv run .gemini/skills/list-pending-issues.py`
- **Description**: Lists all non‑archived issue Markdown files sorted by project name and numeric issue ID.
- **Reuse**: Run this script any time you need an updated list of pending issues.
