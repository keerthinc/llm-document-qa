import os
import faiss
import pickle
from app.embeddings import EmbeddingModel
from app.config import VECTOR_STORE_PATH

embedding_model = EmbeddingModel()

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks

def ingest_documents(folder_path="data/documents"):
    all_chunks = []

    for file in os.listdir(folder_path):
        with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
            text = f.read()
            chunks = chunk_text(text)
            all_chunks.extend(chunks)

    embeddings = embedding_model.embed(all_chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, VECTOR_STORE_PATH)

    with open("vector_store/chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)

    print("Ingestion complete!")
