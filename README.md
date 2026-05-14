# Semantic RAG & Vector Search Assessment

This project implements a local Retrieval-Augmented Generation (RAG) pipeline focused on semantic retrieval, vector search, query expansion, and benchmarking.

The system demonstrates two retrieval strategies:

- Strategy A: Raw Vector Similarity Search
- Strategy B: AI-Enhanced Retrieval using Query Expansion

The project uses local embedding generation, FAISS vector indexing, semantic search, and mocked Vertex AI components to simulate enterprise-grade retrieval workflows.

## Architecture

User Query
    ↓
Query Expansion (Strategy B Only)
    ↓
Embedding Generation
    ↓
FAISS Vector Search
    ↓
Top-K Relevant Chunks
    ↓
Benchmark Comparison

## Tech Stack

- Python
- sentence-transformers
- FAISS
- NumPy
- Pytest

## Features

- Semantic vector search
- Embedding generation using sentence-transformers
- FAISS vector indexing
- Query expansion pipeline
- Retrieval benchmarking
- Mocked Vertex AI SDK behavior
- Automated pytest validation
- JSON and Markdown benchmark reports

## Installation

```bash
git clone <repo-url>

cd semantic-rag-assessment

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt

## Run Project

```bash
python main.py