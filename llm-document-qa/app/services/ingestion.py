import os
import faiss
import pickle
from app.services.embedding import EmbeddingModel
from app.config import VECTOR_STORE_PATH, CHUNK_STORE_PATH

embedding_model = EmbeddingModel()

def chunk_text(text, size=500, overlap=50):
    chunks = []
    for i in range(0, len(text), size - overlap):
        chunks.append(text[i:i+size])
    return chunks

def ingest_documents(folder="data/documents"):
    all_chunks = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            all_chunks.extend(chunk_text(text))

    embeddings = embedding_model.embed(all_chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    os.makedirs("vector_store", exist_ok=True)
    faiss.write_index(index, VECTOR_STORE_PATH)

    with open(CHUNK_STORE_PATH, "wb") as f:
        pickle.dump(all_chunks, f)

    return {"status": "Ingestion complete"}
