import faiss
import pickle
import numpy as np
from rank_bm25 import BM25Okapi
from app.services.embedding import EmbeddingModel
from app.config import VECTOR_STORE_PATH, CHUNK_STORE_PATH

class HybridRetriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.index = faiss.read_index(VECTOR_STORE_PATH)

        with open(CHUNK_STORE_PATH, "rb") as f:
            self.chunks = pickle.load(f)

        tokenized = [doc.split() for doc in self.chunks]
        self.bm25 = BM25Okapi(tokenized)

    def retrieve(self, query, top_k=5):

        # Vector search
        query_embedding = self.embedding_model.embed([query])
        distances, indices = self.index.search(query_embedding, top_k)
        vector_results = [self.chunks[i] for i in indices[0]]

        # BM25 search
        scores = self.bm25.get_scores(query.split())
        top_indices = np.argsort(scores)[-top_k:]
        bm25_results = [self.chunks[i] for i in top_indices]

        return list(set(vector_results + bm25_results))
