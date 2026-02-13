import faiss
import pickle
import os
import requests
from app.config import VECTOR_STORE_PATH, OLLAMA_MODEL, OLLAMA_URL
from app.embeddings import EmbeddingModel

embedding_model = EmbeddingModel()

index = None
chunks = None

def load_vector_store():
    global index, chunks

    if not os.path.exists(VECTOR_STORE_PATH):
        raise Exception("Vector store not found. Run /ingest first.")

    index = faiss.read_index(VECTOR_STORE_PATH)

    with open("vector_store/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

def retrieve(query, top_k=5):
    if index is None:
        load_vector_store()

    query_embedding = embedding_model.embed([query])
    distances, indices = index.search(query_embedding, top_k)

    return [chunks[i] for i in indices[0]]

def generate_answer(query):
    context = "\n\n".join(retrieve(query))

    prompt = f"""
You are a helpful AI assistant.
Answer the question ONLY using the context below.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama error: {response.text}")

    return response.json()["response"]
