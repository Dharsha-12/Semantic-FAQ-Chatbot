"""Create sentence embeddings and save the FAQ collection in ChromaDB."""

from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from faq_data import FAQS


# Keep the local database beside this script so either script can be run
# from a different current working directory.
DATABASE_PATH = Path(__file__).resolve().parent / "chroma_db"
COLLECTION_NAME = "python_faq"
MODEL_NAME = "all-MiniLM-L6-v2"


def main() -> None:
    # Load the sentence-transformer model used for both stored questions and
    # questions typed later in search.py.
    model = SentenceTransformer(MODEL_NAME)

    # PersistentClient writes the vectors and metadata to disk between runs.
    client = chromadb.PersistentClient(path=str(DATABASE_PATH))
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # Embed the FAQ questions, not their answers. A user's question can then
    # be compared with the FAQ questions to find the closest meaning.
    questions = [faq["question"] for faq in FAQS]
    embeddings = model.encode(questions, normalize_embeddings=True)

    # Upsert makes this script safe to run again: existing FAQ IDs are updated
    # instead of being duplicated.
    collection.upsert(
        ids=[faq["id"] for faq in FAQS],
        embeddings=embeddings.tolist(),
        documents=questions,
        metadatas=[{"answer": faq["answer"]} for faq in FAQS],
    )

    print(f"Stored {len(FAQS)} FAQs in '{COLLECTION_NAME}'.")
    print(f"ChromaDB data is saved in: {DATABASE_PATH}")


if __name__ == "__main__":
    main()
