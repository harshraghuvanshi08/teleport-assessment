from rag_main.query_expander import MockGenerativeModel


def test_query_expansion():
    model = MockGenerativeModel()
    query = "How can hallucination be reduced?"
    expanded_query = model.expand_query(query)
    assert "retrieval augmented generation" in expanded_query.lower()
    assert expanded_query != query