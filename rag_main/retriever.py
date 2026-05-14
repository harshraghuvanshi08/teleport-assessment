class Retriever:
    def __init__(self, embedding_model, vector_store, query_expander):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.query_expander = query_expander

    def retrieve_raw(self, query, top_k=3):
        query_embedding = self.embedding_model.embed(query)
        results = self.vector_store.search(query_embedding,top_k=top_k)
        return results

    def retrieve_expanded(self, query, top_k=3):
        expanded_query = self.query_expander.expand_query(query)
        query_embedding = self.embedding_model.embed(expanded_query)
        results = self.vector_store.search(query_embedding,top_k=top_k)
        return {"expanded_query": expanded_query,"results": results}