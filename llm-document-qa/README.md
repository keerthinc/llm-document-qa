# LLM Document Question Answering System (RAG)

A production-ready Retrieval-Augmented Generation (RAG) pipeline built with FastAPI, FAISS, and OpenAI.

## Features

- Document ingestion
- Smart chunking with overlap
- Embedding generation
- Vector similarity search
- LLM-powered contextual answering
- REST API endpoints

# STEP 1 — Create Demo Document

Go to:

```
data/documents/
```

Create a file:

```
ai_rag_demo.txt
```

Paste this inside:

---

##  Document Content 

```
Retrieval-Augmented Generation (RAG) is a technique that improves the accuracy of large language models by combining information retrieval with text generation.

Traditional large language models rely only on their internal training data. This can lead to hallucinations, outdated information, or incorrect answers.

RAG solves this problem by retrieving relevant documents from a knowledge base before generating a response. The system first converts documents into vector embeddings using an embedding model. These embeddings are stored in a vector database such as FAISS.

When a user asks a question, the system converts the query into an embedding and searches the vector database to find the most relevant document chunks. These retrieved chunks are then provided as context to the language model.

The language model generates a response using only the retrieved context. This reduces hallucination and ensures that answers are grounded in real data.

Key Components of a RAG System:
1. Document ingestion and chunking
2. Embedding generation
3. Vector similarity search
4. Context construction
5. Response generation using an LLM

Benefits of RAG:
- Reduces hallucination
- Allows domain-specific knowledge integration
- Keeps information up-to-date
- Improves factual accuracy
- Enables private knowledge base usage

RAG systems are commonly used in enterprise search, document question answering, customer support automation, and internal knowledge assistants.
```

Save the file.

---

# STEP 2 — Make Sure Ollama Is Running

In terminal:

```bash
ollama serve
```

Leave it running.

If already running → fine.

---

# STEP 3 — Start FastAPI

In another terminal:

```bash
cd llm-document-qa
source venv/bin/activate
uvicorn app.main:app --reload
```

You should see:

```
Application startup complete.
Uvicorn running on http://127.0.0.1:8000
```

---

# STEP 4 — Open Swagger UI

Open browser:

```
http://127.0.0.1:8000/docs
```

---

# STEP 5 — Run /ingest

1. Click **POST /ingest**
2. Click **Try it out**
3. Click **Execute**

You should see:

```json
{
  "status": "Documents ingested successfully"
}
```

Now your FAISS index is built.

---

#  STEP 6 — Run /query

Click **POST /query**

Click **Try it out**

Now use these questions 

---

#  Demo Questions (Use These Exactly)

### Question 1

```json
{
  "question": "What is Retrieval-Augmented Generation?"
}
```

---

### Question 2

```json
{
  "question": "What are the key components of a RAG system?"
}
```

---

### Question 3

```json
{
  "question": "Why does RAG reduce hallucination?"
}
```

---

### Question 4 (Guardrail Test)

```json
{
  "question": "Who is the president of France?"
}
```

Expected response:

```
I don't know.
```

That proves your system only answers from context.

---


