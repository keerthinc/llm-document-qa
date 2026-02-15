from fastapi import FastAPI
from app.api.routes_query import router as query_router
from app.api.routes_upload import router as upload_router
from app.api.routes_auth import router as auth_router

app = FastAPI(title="Enterprise RAG System")

app.include_router(query_router)
app.include_router(upload_router)
app.include_router(auth_router)
