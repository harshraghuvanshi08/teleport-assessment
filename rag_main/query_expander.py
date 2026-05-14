class MockGenerativeModel:
    def __init__(self):
        self.expansion_map = {
            "hallucination": "grounded context retrieval augmented generation factual accuracy semantic retrieval document grounding",
            "inference cost": "token optimization quantization batching semantic caching transformer efficiency",
            "retrieval quality": "reranking hybrid search vector similarity query expansion semantic search BM25",
            "latency": "GPU acceleration batching optimization response time inference performance",
            "agentic ai": "tool orchestration reasoning memory planning autonomous AI systems"
            }

    def expand_query(self, query: str):
        expanded_query = query
        query_lower = query.lower()
        for key, item in self.expansion_map.items():
            if key in query_lower:
                expanded_query += " " + item
        return expanded_query