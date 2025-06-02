class VectorStore:
    def __init__(self):
        self.embeddings = {}

    def add_embedding(self, key, vector):
        self.embeddings[key] = vector

    def get_embedding(self, key):
        return self.embeddings.get(key)

    def remove_embedding(self, key):
        if key in self.embeddings:
            del self.embeddings[key]

    def clear(self):
        self.embeddings.clear()

    def all_embeddings(self):
        return self.embeddings.items()