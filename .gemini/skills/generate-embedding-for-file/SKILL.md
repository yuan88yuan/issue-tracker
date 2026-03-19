---
name: generate-embedding-for-file
description: Generates embeddings for a given text file using Ollama with the 'embedding-gemma' model and saves them as a binary file. Use this skill when you need to convert text content from a file into a numerical vector representation for tasks like similarity search, clustering, or classification.
---

# Generate Embedding For File

## Overview

This skill provides the capability to generate numerical embeddings from the text content of a file using a local Ollama server with the `embedding-gemma` model. The resulting embeddings are saved as a binary NumPy (.npy) file, which can be easily loaded and used for various downstream machine learning tasks.

## Prerequisites

To use this skill, you need to have Ollama installed and running on your system, and the `embedding-gemma` model pulled.

1.  **Install Ollama:** Follow the instructions on the official Ollama website (https://ollama.com/download) to install Ollama for your operating system.
2.  **Pull the `embedding-gemma` model:** Once Ollama is installed, open a terminal and run:
    ```bash
    ollama pull embedding-gemma
    ```
3.  **Install Python package:** Ensure you have the `ollama` and `numpy` Python packages installed. If you have `uv` installed, you can use:
    ```bash
    uv pip install ollama numpy
    ```
    Otherwise, use pip:
    ```bash
    pip install ollama numpy
    ```

## Usage

To generate embeddings, use the `generate_embedding.py` script located in the `scripts/` directory.

```bash
python scripts/generate_embedding.py <input_file_path> <output_file_path>
```

- `<input_file_path>`: The path to the text file containing the content for which to generate embeddings.
- `<output_file_path>`: The desired path for the output binary file (e.g., `embeddings.npy`) where the embeddings will be saved.

**Example:**

```bash
python scripts/generate_embedding.py my_document.txt document_embeddings.npy
```

This will read `my_document.txt`, generate its embeddings using Ollama with `embedding-gemma`, and save them to `document_embeddings.npy`.

## Resources

This skill includes the following script:

### scripts/
- `generate_embedding.py`: A Python script that performs the core functionality of generating and saving embeddings.
