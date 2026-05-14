from rag_main.embedding import EmbeddingModel
def test_embedding_generation():
    model = EmbeddingModel()
    embedding = model.embed("Hello AI")
    assert embedding.shape[0] == 1
    assert embedding.shape[1] > 0