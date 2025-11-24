import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_KEY = os.getenv("HF_API_KEY")
HF_MODEL = os.getenv("HF_MODEL", "mistralai/Mistral-7B-Instruct")
HF_TIMEOUT = int(os.getenv("HF_TIMEOUT", "30"))

class LLMComparator:
    def __init__(self, timeout: int = HF_TIMEOUT):
        self.timeout = timeout

    def ask_hf(self, prompt: str) -> str:
        """Call HuggingFace Inference API and return generated text (safe fallback on error)."""
        if not HF_KEY:
            return "Unverifiable"

        url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
        headers = {"Authorization": f"Bearer {HF_KEY}"}
        payload = {"inputs": prompt}

        try:
            r = requests.post(url, headers=headers, json=payload, timeout=self.timeout)
            data = r.json()
            if isinstance(data, list) and "generated_text" in data[0]:
                return data[0]["generated_text"]
            if isinstance(data, dict) and "error" in data:
                return "Unverifiable"
            # Fallback: if API returns plain text
            return str(data)
        except Exception:
            return "Unverifiable"

    def compare(self, claim: str, evidence_list: list) -> str:
        """
        Ask LLM to classify claim vs evidence.
        Returns: "True", "False", or "Unverifiable"
        """
        evidence_text = "\n".join(f"- {e}" for e in evidence_list)
        prompt = f"""
CLAIM:
{claim}

EVIDENCE:
{evidence_text}

Question: Is the CLAIM supported by the EVIDENCE?
Respond with ONE WORD only: True, False, or Unverifiable.
"""
        raw = self.ask_hf(prompt).strip()
        for label in ["True", "False", "Unverifiable"]:
            if label.lower() in raw.lower():
                return label
        return "Unverifiable"

    def generate_reasoning(self, claim: str, evidence_list: list, verdict: str) -> str:
        """
        Generate a short, 1-2 sentence reasoning for the verdict.
        If HF key missing, return a deterministic fallback explanation.
        """
        if not HF_KEY:
            if verdict == "Likely True":
                return "Retrieved facts in the trusted dataset match the claim's content."
            if verdict == "Likely False":
                return "Retrieved facts contradict the claim's content."
            return "Available evidence does not confirm or deny the claim."

        evidence_text = "\n".join(f"- {e}" for e in evidence_list)
        prompt = f"""
CLAIM:
{claim}

EVIDENCE:
{evidence_text}

VERDICT: {verdict}

Write a short (1-2 sentence) explanation why the verdict was chosen.
"""
        return self.ask_hf(prompt).strip()