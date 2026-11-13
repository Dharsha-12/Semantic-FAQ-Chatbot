"""Ask questions in the terminal and retrieve the closest FAQ from ChromaDB."""

from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


# These settings must match those in store_embeddings.py.
DATABASE_PATH = Path(__file__).resolve().parent / "chroma_db"
COLLECTION_NAME = "python_faq"
MODEL_NAME = "all-MiniLM-L6-v2"


def main() -> None:
    # Load the same embedding model used when the FAQ questions were stored.
    model = SentenceTransformer(MODEL_NAME)
    client = chromadb.PersistentClient(path=str(DATABASE_PATH))
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # Give a clear setup instruction instead of attempting a search with no data.
    if collection.count() == 0:
        raise RuntimeError(
            "The FAQ collection is empty. Run 'python store_embeddings.py' first."
        )

    print("FAQ chatbot is ready. Type 'quit' or 'exit' to stop.")

    # Read questions until the user chooses to leave.
    while True:
        user_question = input("\nYour question: ").strip()
        if user_question.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not user_question:
            print("Please enter a question.")
            continue

        # Convert the user's question into the same kind of vector as the FAQs.
        query_embedding = model.encode(
            user_question,
            normalize_embeddings=True,
        )

        # ChromaDB returns the closest stored question, its answer metadata,
        # and its cosine distance. Asking for one result gives the top match.
        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=1,
            include=["documents", "metadatas", "distances"],
        )

        matched_question = results["documents"][0][0]
        matched_metadata = results["metadatas"][0][0]
        cosine_distance = results["distances"][0][0]

        # Cosine distance is 1 - cosine similarity, so a higher similarity
        # score means the two question vectors are closer in meaning.
        similarity_score = 1.0 - cosine_distance

        print(f"Closest FAQ: {matched_question}")
        print(f"Answer: {matched_metadata['answer']}")
        print(f"Similarity score (cosine similarity): {similarity_score:.4f}")


if __name__ == "__main__":
    main()
