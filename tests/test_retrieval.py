from rag_main.embedding import EmbeddingModel
from rag_main.store_vector import VectorStore
from rag_main.query_expander import MockGenerativeModel
from rag_main.retriever import Retriever


def test_retrieval_pipeline():
    chunks = [
        "RAG improves factual accuracy using external documents.",
        "GPU acceleration improves transformer inference.",
        "Query expansion improves semantic retrieval."
    ]
    embedding_model = EmbeddingModel()
    embeddings = embedding_model.embed(chunks)
    vector_store = VectorStore(dimension=embeddings.shape[1])
    vector_store.add_embeddings(embeddings, chunks)

    query_expander = MockGenerativeModel()
    retriever = Retriever(embedding_model, vector_store, query_expander)

    results = retriever.retrieve_raw("How does query expansion help retrieval?")
    assert len(results) > 0
    assert "query expansion" in (results[0]["chunk"].lower())