from fastapi import APIRouter, UploadFile, File
from app.services.ingestion import ingest_documents
import os

router = APIRouter()

@router.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    os.makedirs("data/documents", exist_ok=True)

    for file in files:
        content = await file.read()
        with open(f"data/documents/{file.filename}", "wb") as f:
            f.write(content)

    return ingest_documents()
