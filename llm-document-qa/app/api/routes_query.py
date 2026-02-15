from fastapi import APIRouter
from pydantic import BaseModel
from app.core.hybrid_retriever import HybridRetriever
from app.core.reranker import ReRanker
from app.core.llm_service import generate, stream
from app.core.memory import save_message

router = APIRouter()

#retriever = HybridRetriever()
reranker = ReRanker()

class Query(BaseModel):
    question: str
    session_id: str = "default"

@router.post("/query")
def query(q: Query):

    retriever = HybridRetriever()
    reranker = ReRanker()

    docs = retriever.retrieve(q.question)
    ranked = reranker.rerank(q.question, docs)

    context = "\n\n".join(ranked[:5])

    prompt = f"""
Answer only using the context below.

Context:
{context}

Question:
{q.question}
"""

    answer = generate(prompt)

    save_message(q.session_id, q.question)
    save_message(q.session_id, answer)

    return {"answer": answer}



@router.post("/query/stream")
def query_stream(q: Query):

    docs = retriever.retrieve(q.question)
    ranked = reranker.rerank(q.question, docs)
    context = "\n\n".join(ranked[:5])

    prompt = f"""
Answer only using the context below.

Context:
{context}

Question:
{q.question}
"""

    return stream(prompt)
