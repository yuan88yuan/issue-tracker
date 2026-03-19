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

## 4. Knowledge Base Workflow

This project incorporates a knowledge base for each project to store solutions, technical documentation, troubleshooting guides, and FAQs.

### 4.1. Directory Structure
- **Root**: `issues/`
- **Project Specific**: `issues/[project-name]/`
- **Knowledge Base Directory**: `issues/[project-name]/kb/`
- **Template**: `issues/KB_TEMPLATE.md` (Refer to this for all new knowledge base article structures)
- **Naming Convention**: `KB-[ID]-[short-kebab-case-description].md` (e.g., `KB-001-common-boot-issues.md`)

### 4.2. Professional Writing Standards for Knowledge Base Articles
When creating or updating knowledge base articles, you MUST adhere to the following standards:
- **Tone**: Technical, clear, concise, and informative.
- **Structure**: Always use the defined `KB_TEMPLATE.md`.
- **Focus**: Provide actionable information, solutions, explanations, and relevant technical details.
- **Clarity**: Ensure easy understanding for technical and non-technical audiences where appropriate.

### 4.3. Operational Workflow for Knowledge Base
1. **Creation**: If a project's knowledge base directory does not exist, create it using `mkdir -p issues/[project-name]/kb/`.
2. **Implementation**: Use `write_file` for new articles or `replace` for updates.
3. **Autonomy**: Proactively fill in relevant technical details and step-by-step instructions based on the context provided.

## 5. Archiving Workflow

When an issue is resolved and marked with "Status: Closed" within its content, it MUST be archived.

### 5.1. Directory Structure
- **Archive Directory**: `issues/[project-name]/archive/`

### 5.2. Naming Convention
- Archived issues MUST be renamed by prepending `CLOSED-` to their original filename (e.g., `ISSUE-001-boot-hang.md` becomes `CLOSED-ISSUE-001-boot-hang.md`).

### 5.3. Operational Workflow
1. **Identification**: Identify issues with "Status: Closed" in their content.
2. **Creation**: If the `archive/` directory does not exist for a given project, create it using `mkdir -p issues/[project-name]/archive/`.
3. **Archiving**: Move the identified issue file to the respective `issues/[project-name]/archive/` directory and rename it according to the naming convention.
