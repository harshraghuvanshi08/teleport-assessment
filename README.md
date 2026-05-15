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
git clone https://github.com/harshraghuvanshi08/teleport-assessment.git

cd semantic-rag-assessment

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

## Run Project
```bash
python main.py
```

## Similarity Metric Choice

This project uses Cosine Similarity for semantic retrieval.

Why Cosine Similarity?

- Text embeddings primarily encode semantic direction rather than vector magnitude.
- Cosine similarity measures angular similarity between embeddings.
- It performs better for NLP and semantic search tasks compared to Euclidean distance.

Implementation Details:

- FAISS IndexFlatIP is used for inner-product similarity.
- Embeddings are L2-normalized before indexing.
- After normalization, inner product becomes equivalent to cosine similarity.

Why Not Euclidean Distance?

Euclidean distance is sensitive to vector magnitude and scaling differences, which makes it less suitable for semantic embedding comparison.


## Production Migration to Vertex AI

This local implementation can be migrated to Google Cloud Vertex AI as follows:

| Local Component | Vertex AI Equivalent |
|---|---|
| sentence-transformers | textembedding-gecko |
| FAISS | Vertex AI Matching Engine |
| MockGenerativeModel | Gemini |
| Local Retrieval Pipeline | Vertex AI Retrieval Architecture |

Production Workflow:

1. User query received
2. Gemini rewrites or expands query
3. textembedding-gecko generates embeddings
4. Vertex AI Matching Engine performs semantic retrieval
5. Retrieved context passed to Gemini
6. Final grounded response generated

Additional Production Enhancements:

- Hybrid Search (BM25 + Dense Retrieval)
- Metadata filtering
- Cross-encoder reranking
- Retrieval observability
- Semantic caching
- Distributed vector indexing

## Benchmark Findings

The benchmark results demonstrate that query expansion improves retrieval relevance by enriching semantic context before embedding generation.

Observed Improvements:

- Better retrieval recall
- Higher semantic alignment
- Improved ranking quality
- More contextually relevant chunks

Strategy B consistently retrieved more relevant AI-related context compared to raw vector search.

## Future Improvements

- Hybrid Retrieval (BM25 + Dense Search)
- Cross-Encoder Reranking
- Multi-Query Retrieval
- HyDE Query Expansion
- Streaming Retrieval
- Metadata-aware Search
- Distributed FAISS Indexing
- Real-time Embedding Pipelines

