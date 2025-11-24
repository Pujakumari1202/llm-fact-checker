import os
import pandas as pd
from src.embedder import Embedder
from src.retriever import Retriever
from src.llm_compare import LLMComparator

class FactCheckPipeline:
    def __init__(self, facts_csv: str = "data/facts.csv", persist_dir: str = "chroma_db"):
        # Load facts CSV (expects plain_text column)
        if not os.path.exists(facts_csv):
            raise FileNotFoundError(f"Facts CSV not found at {facts_csv}")
        df = pd.read_csv(facts_csv, on_bad_lines="skip")
        self.fact_texts = df["plain_text"].astype(str).tolist()

        # Components
        self.embedder = Embedder(device="cpu")
        self.retriever = Retriever(persist_dir=persist_dir)
        self.llm = LLMComparator()

        # Ensure facts are stored in ChromaDB
        self._ensure_index()

    def _ensure_index(self):
        """
        If ChromaDB collection is empty, embed and add documents.
        """
        # naive check: query with a zero vector to see if there are any documents
        existing = self.retriever.collection.count()
        if existing >= len(self.fact_texts):
            return  # already populated

        embeddings = self.embedder.encode(self.fact_texts)
        ids = [str(i) for i in range(len(self.fact_texts))]
        self.retriever.add_documents(ids=ids, documents=self.fact_texts, embeddings=embeddings)

    def run(self, user_text: str) -> dict:
        """
        Run pipeline for a single claim string.
        Returns: {"verdict":..., "evidence":[...], "reasoning":...}
        """
        claim = user_text.strip()
        if not claim:
            return {"verdict": "Unverifiable", "evidence": [], "reasoning": "No claim provided."}

        # Embed and query
        query_vec = self.embedder.encode([claim])[0]
        evidence = self.retriever.get_top_k(query_vec, k=3)
        if not evidence:
            evidence = ["No evidence found in the trusted fact base."]

        # LLM compare + reasoning
        raw_label = self.llm.compare(claim, evidence)  # "True"/"False"/"Unverifiable"
        verdict_map = {"True": "Likely True", "False": "Likely False", "Unverifiable": "Unverifiable"}
        verdict = verdict_map.get(raw_label, "Unverifiable")
        reasoning = self.llm.generate_reasoning(claim, evidence, verdict)

        return {"verdict": verdict, "evidence": evidence, "reasoning": reasoning}

# Quick local test guard
if __name__ == "__main__":
    p = FactCheckPipeline()
    print(p.run("India achieved record food grain output in 2025."))