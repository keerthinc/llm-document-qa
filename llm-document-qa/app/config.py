import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

VECTOR_STORE_PATH = "vector_store/faiss.index"
CHUNK_STORE_PATH = "vector_store/chunks.pkl"

OLLAMA_MODEL = "phi3"
OLLAMA_URL = "http://localhost:11434/api/generate"

REDIS_HOST = "localhost"
REDIS_PORT = 6379

SECRET_KEY = "supersecret"
