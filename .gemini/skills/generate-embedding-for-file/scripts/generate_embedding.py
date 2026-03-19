import argparse
import numpy as np
import ollama

def generate_embeddings(text: str, model_name: str = "embeddinggemma"):
    """Generates embeddings for a given text using Ollama."""
    try:
        response = ollama.embeddings(model=model_name, prompt=text)
        return response['embedding']
    except Exception as e:
        print(f"Error generating embeddings with Ollama: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate embeddings for a text file using Ollama with the embedding-gemma model.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("output_file", help="Path to the output binary file for embeddings (.npy format recommended).")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        text_content = f.read()

    if not text_content.strip():
        print("Input file is empty or contains only whitespace. No embeddings generated.")
        return

    embeddings = generate_embeddings(text_content)

    if embeddings is not None:
        np.save(args.output_file, np.array(embeddings))
        print(f"Embeddings successfully generated and saved to {args.output_file}")
    else:
        print("Failed to generate embeddings.")

if __name__ == "__main__":
    main()
