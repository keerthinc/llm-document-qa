# Fully Local RAG System with Ollama + FAISS

A production-ready **Retrieval-Augmented Generation (RAG)** pipeline built using:

- FastAPI (API layer)
- FAISS (Vector Database)
- Hybrid Search (BM25 + Vector)
- Cross-Encoder Re-ranking
- Ollama (Local LLM - phi3)
- Redis (Caching + Memory)
- Streaming responses

This system runs **100% locally** — no external API dependency, no OpenAI billing, fully offline.

---

## Architecture Overview

```

User Query
↓
Hybrid Retriever (FAISS + BM25)
↓
Re-Ranker (Cross Encoder)
↓
Context Builder
↓
Ollama (phi3 - Local LLM)
↓
Streaming / Cached Response
↓
Redis Memory Storage

```

---

## Features

- Hybrid Search (BM25 + Vector similarity)
- Cross-Encoder Re-ranking
- Fully local LLM (phi3 via Ollama)
- Redis caching
- Conversation memory
- Multi-document upload API
- Streaming responses
- JWT Authentication
- Modular production structure

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-purple)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)
![Redis](https://img.shields.io/badge/Redis-Cache-red)

---

# Project Structure

```

llm-document-qa/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── config.py
│   └── main.py
│
├── data/documents/
├── vector_store/
├── requirements.txt
└── README.md

````

---

# How RAG Works in This Project

1. Documents are uploaded
2. Text is chunked
3. Embeddings are generated
4. Stored in FAISS
5. Query is embedded
6. Hybrid retrieval (BM25 + vector)
7. Re-ranking applied
8. Context passed to local LLM (phi3)
9. Response generated and cached
10. Memory stored in Redis

---

# Setup Instructions

## STEP 1 — Install Dependencies

```bash
pip install -r requirements.txt
````

---

## STEP 2 — Install Ollama

Install Ollama:

```bash
brew install ollama
```

Pull model:

```bash
ollama pull phi3
```

Start Ollama:

```bash
ollama serve
```

Leave it running.

---

## STEP 3 — Start Redis

Using Docker:

```bash
docker run -p 6379:6379 redis
```

---

## STEP 4 — Start FastAPI

```bash
uvicorn app.main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## STEP 5 — Open Swagger UI

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

# Demo: Create Sample Document

Go to:

```
data/documents/
```

Create:

```
ai_rag_demo.txt
```

Paste this:

```
Retrieval-Augmented Generation (RAG) is a technique that improves the accuracy of large language models by combining information retrieval with text generation.

Traditional large language models rely only on their internal training data. This can lead to hallucinations or outdated answers.

A RAG system works by first converting documents into vector embeddings using an embedding model. These embeddings are stored in a vector database such as FAISS.

When a user asks a question, the system retrieves the most relevant document chunks using vector similarity search and optionally BM25 keyword search.

The retrieved context is then passed to a language model to generate a grounded answer.

Key components of a RAG system include:
1. Document ingestion
2. Text chunking
3. Embedding generation
4. Vector similarity search
5. Re-ranking
6. Context-aware generation
```

Save the file.

---

# STEP 6 — Upload Document

In Swagger UI:

* Click `POST /upload`
* Click **Try it out**
* Upload `ai_rag_demo.txt`
* Click **Execute**

You should see:

```json
{
  "status": "Ingestion complete"
}
```

---

# STEP 7 — Ask Questions

Use `POST /query`

### Question 1

```json
{
  "question": "What is Retrieval-Augmented Generation?",
  "session_id": "user1"
}
```

---

### Question 2

```json
{
  "question": "What are the key components of a RAG system?",
  "session_id": "user1"
}
```

---

### Question 3 (Guardrail Test)

```json
{
  "question": "Who is the president of France?",
  "session_id": "user1"
}
```

Expected:

```
I don't know.
```

This proves the system only answers from retrieved context.

---

# Streaming Endpoint

Use:

```
POST /query/stream
```

This streams tokens live from the local LLM.

---

# Production Concepts Implemented

* Hybrid Retrieval
* Re-ranking
* Prompt grounding
* Guardrail design
* LLM caching
* Conversation memory
* Modular API design
* Local model serving

---

# Why This Project Is Strong

Unlike basic RAG demos, this system:

* Does not rely on external APIs
* Uses hybrid search instead of pure vector search
* Applies cross-encoder re-ranking
* Implements streaming
* Includes caching and memory
* Follows production-style modular architecture

---

# Summary

> Built a fully local Retrieval-Augmented Generation (RAG) system using FAISS, BM25 hybrid retrieval, cross-encoder re-ranking, and a locally served LLM (phi3 via Ollama). Implemented streaming responses, Redis caching, and modular FastAPI architecture for scalable document question answering.

---

# uture Improvements

* RAGAS evaluation pipeline
* Frontend chat interface
* Dockerized full stack deployment
* Kubernetes deployment
* Observability (Prometheus + Grafana)
* Vector DB migration (Qdrant / Weaviate)

---
