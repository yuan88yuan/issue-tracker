# AGENTS.md - Agentic Coding Guidelines

This document provides guidelines for agentic coding agents operating in this repository.

## 1. Project Overview

This repository is a professional issue tracking system using Markdown documentation. It contains:
- Issue documentation in `issues/[project-name]/`
- Knowledge base articles in `issues/[project-name]/kb/`
- Python scripts for embedding generation (`.gemini/skills/`)
- Main application code in `main.py` and supporting modules

## 2. Build/Lint/Test Commands

### Python Environment
```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies (if any)
uv sync
```

### Running Python Scripts
```bash
# Run main application
python main.py

# Run specific scripts
python generate_all_embeddings.py
python check_packages.py

# Run skill scripts
python .gemini/skills/search-issues-by-embedding/scripts/search_issues.py
python .gemini/skills/generate-embedding-for-file/scripts/generate_embedding.py
```

### Testing (if tests exist)
```bash
# Run all tests with pytest
pytest

# Run a single test file
pytest tests/test_file.py

# Run a specific test function
pytest tests/test_file.py::test_function_name

# Run tests matching a pattern
pytest -k "test_pattern"
```

### Linting/Formatting
```bash
# Run ruff linter (if installed)
ruff check .

# Run ruff with auto-fix
ruff check --fix .

# Format with ruff
ruff format .

# Run mypy type checker (if installed)
mypy .
```

### Pre-commit Hooks (if configured)
```bash
pre-commit run --all-files
```

## 3. Code Style Guidelines

### General Principles
- Write clean, readable, and maintainable code
- Keep functions small and focused (single responsibility)
- Use meaningful variable and function names
- Add type hints for function arguments and return values
- Prefer explicit over implicit

### Python Style (PEP 8)
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use snake_case for variable/function names
- Use PascalCase for class names
- Use ALL_CAPS for constants
- Two blank lines between top-level definitions
- One blank line between method definitions in a class

### Imports
```python
# Standard library imports first
import os
import sys
from typing import List, Dict, Optional

# Third-party imports second
import numpy as np
from pathlib import Path

# Local/application imports last
from module import something

# Group imports by type with blank lines between groups
# Avoid wildcard imports (e.g., from module import *)
```

### Type Hints
```python
# Always use type hints for function signatures
def process_items(items: List[str]) -> Dict[str, int]:
    ...

# Use Optional for nullable types (not Union[...])
def maybe_get_value(key: str) -> Optional[str]:
    ...

# Use TypeAlias for complex types
Vector = List[float]
```

### Naming Conventions
- Variables: `snapshot_count`, `max_buffer_size`
- Functions: `get_issue_by_id()`, `process_embedding()`
- Classes: `IssueTracker`, `EmbeddingGenerator`
- Constants: `MAX_RETRIES = 3`, `DEFAULT_TIMEOUT = 30`
- Files: `issue_tracker.py`, `embedding_generator.py`

### Error Handling
```python
# Use specific exception types
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise MyCustomError("Fallback message") from e
except Exception as e:
    logger.exception("Unexpected error")
    raise

# Never silently except Exception or BaseException
# Always log or re-raise
```

### Documentation
- Use docstrings for public APIs
- Keep docstrings concise but informative
- Follow Google or NumPy docstring format
- Document exceptions that functions can raise

```python
def calculate_embedding(text: str) -> np.ndarray:
    """Generate embedding vector for input text.

    Args:
        text: Input string to generate embedding for.

    Returns:
        Numpy array containing the embedding vector.

    Raises:
        ValueError: If input text is empty.
    """
```

### Performance
- Use list/dict comprehensions where appropriate
- Avoid premature optimization
- Profile before optimizing
- Use generators for large datasets

### Testing
- Write unit tests for all public functions
- Use descriptive test names: `test_issue_creation_fails_with_empty_title()`
- Use fixtures for shared test data
- Aim for high test coverage on business logic
- Keep tests fast and independent

## 4. Markdown Documentation Style

For issue tracking and knowledge base articles:

### Issue Files (`issues/[project]/ISSUE-*.md`)
- Always use `ISSUE_TEMPLATE.md` as the base
- Fill in all required fields
- Use clear, technical language
- Include reproduction steps for bugs
- Define specific acceptance criteria

### Knowledge Base (`issues/[project]/kb/KB-*.md`)
- Always use `KB_TEMPLATE.md` as the base
- Focus on actionable solutions
- Include code examples where relevant
- Add keywords for searchability

### General Markdown Rules
- Use ATX-style headers (#, ##, ###)
- Use fenced code blocks with language identifiers
- Use tables for structured data
- Keep lines reasonably short (max 120 chars)
- Use bullet points for lists
- Avoid excessive emphasis

## 5. Git Workflow

- Make commits atomic and descriptive
- Use conventional commit format if applicable
- Run linting before committing
- Don't commit generated files (embeddings, .npy files)
- Don't commit secrets or credentials

## 6. Dependencies

- Python 3.13+
- Dependencies managed via `pyproject.toml`
- Use `uv` for package management
- Keep dependencies minimal

## 7. File Organization

```
/home/zzlee/docker/issue-tracker/
├── AGENTS.md              # This file
├── GEMINI.md              # Issue tracking workflow mandates
├── README.md              # Project documentation
├── pyproject.toml         # Python project config
├── main.py                # Entry point
├── issues/                # Issue documentation
│   ├── ISSUE_TEMPLATE.md
│   ├── KB_TEMPLATE.md
│   └── [project-name]/
│       ├── ISSUE-*.md
│       ├── kb/KB-*.md
│       └── archive/
└── .gemini/               # Skills and scripts
    └── skills/
```

## 8. References

- See `GEMINI.md` for issue tracking workflow mandates
- See `issues/ISSUE_TEMPLATE.md` for issue structure
- See `issues/KB_TEMPLATE.md` for knowledge base article structure