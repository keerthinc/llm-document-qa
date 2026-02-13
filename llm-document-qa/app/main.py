from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import generate_answer
from app.ingest import ingest_documents

app = FastAPI(title="LLM Document QA System")

class QueryRequest(BaseModel):
    question: str

@app.post("/ingest")
def ingest():
    ingest_documents()
    return {"status": "Documents ingested successfully"}

@app.post("/query")
def query(request: QueryRequest):
    answer = generate_answer(request.question)
    return {"answer": answer}
