from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

class Embedder:
    def __init__(self, device: str = "cpu"):
        # Load model once
        self.model = SentenceTransformer(MODEL_NAME, device=device)

    def encode(self, texts):
        """
        Encode a list of texts to numpy embeddings.
        Args:
            texts: list[str]
        Returns:
            numpy.ndarray
        """
        return self.model.encode(texts, convert_to_numpy=True)