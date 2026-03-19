import argparse
import os
import numpy as np
import ollama
from sklearn.metrics.pairwise import cosine_similarity

def generate_query_embedding(query: str, model_name: str = "embeddinggemma"):
    """Generates an embedding for the search query using Ollama."""
    try:
        response = ollama.embeddings(model=model_name, prompt=query)
        return np.array(response['embedding']).reshape(1, -1)
    except Exception as e:
        print(f"Error generating query embedding with Ollama: {e}")
        return None

def load_issue_embeddings(base_dir: str):
    """Loads all issue embeddings from specified directories."""
    all_embeddings = []
    issue_paths = []
    
    for root, _, files in os.walk(base_dir):
        if "embeddings" in root and root.endswith("embeddings"):
            project_path = os.path.dirname(root)
            for file in files:
                if file.endswith(".npy"):
                    embedding_path = os.path.join(root, file)
                    issue_filename_without_ext = os.path.splitext(file)[0]
                    issue_path = os.path.join(project_path, issue_filename_without_ext + ".md")
                    
                    try:
                        embedding = np.load(embedding_path)
                        all_embeddings.append(embedding)
                        issue_paths.append(issue_path)
                    except Exception as e:
                        print(f"Error loading embedding from {embedding_path}: {e}")
    
    return np.array(all_embeddings), issue_paths

def main():
    parser = argparse.ArgumentParser(description="Search for similar issues based on an embedding match.")
    parser.add_argument("--query", required=True, help="The search query text.")
    parser.add_argument("--top_n", type=int, default=5, help="Number of top matching issues to display.")

    args = parser.parse_args()

    # Generate embedding for the query
    query_embedding = generate_query_embedding(args.query)
    if query_embedding is None:
        return

    # Load all issue embeddings
    base_issues_dir = "issues"
    issue_embeddings, issue_paths = load_issue_embeddings(base_issues_dir)

    if len(issue_embeddings) == 0:
        print("No issue embeddings found. Please generate embeddings first.")
        return

    # Calculate cosine similarity
    similarities = cosine_similarity(query_embedding, issue_embeddings)[0]

    # Rank and display results
    ranked_indices = np.argsort(similarities)[::-1] # Sort in descending order
    print() # Add a newline
    print(f"Top {args.top_n} most similar issues for query: '{args.query}'")
    print("--------------------------------------------------")

    for i, idx in enumerate(ranked_indices[:args.top_n]):
        print(f"{i+1}. Similarity: {similarities[idx]:.4f} - {issue_paths[idx]}")

if __name__ == "__main__":
    main()
