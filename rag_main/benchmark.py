import json

class RetrievalBenchmark:
    def __init__(self, retriever):
        self.retriever = retriever
        self.queries = [
            "How can hallucinations be reduced in LLM systems?",
            "How do AI systems reduce inference cost?",
            "How is retrieval quality improved in RAG pipelines?"
        ]

    def run_benchmark(self):
        benchmark_results = []
        for query in self.queries:
            raw_results = self.retriever.retrieve_raw(query) # Strategy A
            expanded_results = self.retriever.retrieve_expanded(query) # Strategy B
            benchmark_results.append({"query": query,"strategy_a": raw_results, "strategy_b": {"expanded_query":expanded_results["expanded_query"], "results":expanded_results["results"]}})
        return benchmark_results

    def save_json(self, benchmark_results, filepath="benchmark_results.json"):
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(benchmark_results, file, indent=4)

    def save_markdown(self, benchmark_results, filepath="retrieval_benchmark.md"):
        with open(filepath, "w", encoding="utf-8") as file:
            file.write("# Retrieval Benchmark Report\n\n")
            for item in benchmark_results:
                file.write(f"## Query\n")
                file.write(f"{item['query']}\n\n")
                file.write("### Strategy A — Raw Vector Search\n\n") # Strategy A
                for idx, result in enumerate(item["strategy_a"], start=1):
                    file.write(f"{idx}. " + f"(Score: {result['score']:.4f})\n\n")
                    file.write(f"{result['chunk']}\n\n")
                file.write("### Strategy B — Query Expansion\n\n") # Strategy B
                file.write(f"**Expanded Query:**\n\n")
                file.write(f"{item['strategy_b']['expanded_query']}\n\n")
                for idx, result in enumerate(item["strategy_b"]["results"], start=1):
                    file.write(f"{idx}. " + f"(Score: {result['score']:.4f})\n\n")
                    file.write(f"{result['chunk']}\n\n")
                file.write("---\n\n")