# GEMINI Mandates: Issue Tracking Workflow

This project is dedicated to tracking software issues using high-signal, professional Markdown documentation. All interactions regarding issue management must strictly adhere to these rules.

## 1. Directory Structure
- **Root**: `issues/`
- **Template**: `issues/ISSUE_TEMPLATE.md` (Refer to this for all new issue structures)
- **Project Specific**: `issues/[project-name]/`
- **Naming Convention**: `ISSUE-[ID]-[short-kebab-case-description].md` (e.g., `ISSUE-001-boot-hang.md`)

## 2. Professional Rewriting Standards
When the user provides a raw issue description, you MUST rewrite it as an expert software engineer.
- **Tone**: Technical, precise, and objective.
- **Structure**: Always use the defined template.
- **Focus**: Emphasize impact, technical suspicion (e.g., race conditions, hardware synchronization), and clear acceptance criteria.
- **Efficiency**: Avoid filler; prioritize actionable technical data (e.g., JTAG strategies, MMIO concerns).

## 3. Operational Workflow
1. **Creation**: If a project directory does not exist, create it using `mkdir -p issues/[project-name]`.
2. **Implementation**: Use `write_file` for new issues or `replace` for updates.
3. **Autonomy**: Proactively fill in likely technical suspicions and diagnostic strategies based on the context provided, while marking them as (Optional) or needing verification.
