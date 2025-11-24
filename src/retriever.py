import os
import numpy as np
import chromadb
from chromadb.config import Settings

class Retriever:
    def __init__(self, collection_name="facts_collection", persist_dir="chroma_db"):
        """
        Initialize Chroma client and collection (persistent).
        """
        os.makedirs(persist_dir, exist_ok=True)
        settings = Settings(persist_directory=persist_dir)
        self.client = chromadb.Client(settings=settings)

        # Create or get collection
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_documents(self, ids, documents, embeddings):
        """
        Add documents + embeddings to the collection.
        Args:
            ids: list[str]
            documents: list[str]
            embeddings: numpy.ndarray or list[list[float]]
        """
        # chromadb expects embeddings as lists
        emb_list = embeddings.tolist() if hasattr(embeddings, "tolist") else embeddings
        self.collection.add(ids=ids, documents=documents, embeddings=emb_list)

    def get_top_k(self, query_embedding, k=3, include_documents=True):
        """
        Query the collection with a single embedding and return top-k documents.
        Returns: list[str] (documents)
        """
        # Query returns a dict with 'documents' and 'distances' etc.
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            include=["documents", "distances"]
        )
        docs = results.get("documents", [[]])[0]
        return docs