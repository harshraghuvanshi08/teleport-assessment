from rag_main.embedding import EmbeddingModel
from rag_main.store_vector import VectorStore
from rag_main.data import DatasetLoader
from rag_main.query_expander import MockGenerativeModel
from rag_main.retriever import Retriever
from rag_main.benchmark import RetrievalBenchmark


# Load dataset
loader = DatasetLoader("main/doc.txt")

chunks = loader.load_chunks()


# Initialize embedding model
embedding_model = EmbeddingModel()

# Generate embeddings
embeddings = embedding_model.embed(chunks)


# Initialize vector store
vector_store = VectorStore(
    dimension=embeddings.shape[1]
)

vector_store.add_embeddings(
    embeddings,
    chunks
)


# Initialize query expander
query_expander = MockGenerativeModel()


# Initialize retriever
retriever = Retriever(
    embedding_model,
    vector_store,
    query_expander
)


# Run benchmark
benchmark = RetrievalBenchmark(retriever)

results = benchmark.run_benchmark()


# Save outputs
benchmark.save_json(results)

benchmark.save_markdown(results)


print("\nBenchmark completed successfully.")
print("Generated:")
print("- benchmark_results.json")
print("- retrieval_benchmark.md")