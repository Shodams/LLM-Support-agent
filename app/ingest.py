"""
Handles:
- Loading dataset
- Converting to documents
- Creating FAISS vector store
"""

import json
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from app.config import EMBEDDING_MODEL, VECTOR_DB_PATH


def load_data():
    with open("data/dataset.json") as f:
        return json.load(f)


def create_documents(data):
    documents = []

    for item in data:
        content = f"Q: {item['question']}\nA: {item['answer']}"
        documents.append(Document(page_content=content))

    return documents


def build_vector_store():
    print("Loading data...")
    data = load_data()

    print("Creating documents...")
    docs = create_documents(data)

    print("Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    print("Building FAISS index...")
    vectorstore = FAISS.from_documents(docs, embeddings)

    print("Saving vector store...")
    vectorstore.save_local(VECTOR_DB_PATH)

    print("Done!")


if __name__ == "__main__":
    build_vector_store()
