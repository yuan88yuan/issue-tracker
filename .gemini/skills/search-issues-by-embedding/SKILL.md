---
name: search-issues-by-embedding
description: Searches for similar issues based on an embedding match using Ollama's 'embeddinggemma' model.
---

# Search Issues by Embedding

## Overview

This skill allows you to search for software issues that are semantically similar to a given query. It leverages the 'embeddinggemma' model from Ollama to generate embeddings for your search query and compares them against pre-generated embeddings of existing issues. The skill then ranks and displays the most similar issues.

## Prerequisites

To use this skill, you need to have:

1.  **Ollama installed and running** on your system.
2.  The `embeddinggemma` model pulled in Ollama:
    ```bash
    ollama pull embeddinggemma
    ```
3.  **Python packages installed:** `ollama`, `numpy`, and `scikit-learn`. If you have `uv` installed, you can use:
    ```bash
    uv pip install ollama numpy scikit-learn
    ```
    Otherwise, use pip:
    ```bash
    pip install ollama numpy scikit-learn
    ```
4.  **Issue embeddings generated:** Before searching, you must have generated embeddings for your issues using the `generate-embedding-for-file` skill. These embeddings should be located in `issues/[project-name]/embeddings/` directories.

## Usage

To search for similar issues, use the `search_issues.py` script located in the `scripts/` directory.

```bash
.venv/bin/python .gemini/skills/search-issues-by-embedding/scripts/search_issues.py --query "<your_search_query>" [--top_n <number_of_results>]
```

- `--query`: The text of your search query. This is a required argument.
- `--top_n`: (Optional) The number of top matching issues to display. Defaults to 5.

**Example:**

```bash
.venv/bin/python .gemini/skills/search-issues-by-embedding/scripts/search_issues.py --query "problems with video encoding" --top_n 3
```

This will search for issues similar to "problems with video encoding" and display the top 3 matches.

## Resources

This skill includes the following script:

### scripts/
- `search_issues.py`: A Python script that performs the core functionality of searching and ranking issues by embedding similarity.
