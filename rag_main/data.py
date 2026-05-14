class DatasetLoader:
    def __init__(self, filepath):
        self.filepath = filepath
    def load_chunks(self):
        with open(self.filepath, "r", encoding="utf-8") as file:
            text = file.read()
        chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
        return chunks
    
    