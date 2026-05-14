class TextEmbeddingModel:
    @classmethod
    def from_pretrained(cls, model_name):
        return cls()
    
    def get_embeddings(self, texts):
        return [{"embedding": [0.1, 0.2, 0.3]} for _ in texts]

class GenerativeModel:
    def __init__(self, model_name):
        self.model_name = model_name
    def generate_content(self, prompt):
        return {"text":f"Expanded query for: {prompt}"}