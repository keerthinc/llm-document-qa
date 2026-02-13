import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
VECTOR_STORE_PATH = "vector_store/faiss.index"

OLLAMA_MODEL = "phi3"
OLLAMA_URL = "http://localhost:11434/api/generate"
