import streamlit as st
from src.pipeline import FactCheckPipeline
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


# Streamlit page settings
st.set_page_config(page_title="LLM Fact Checker", layout="centered")

@st.cache_resource
def load_pipeline():
    """
    Loads and caches the FactCheckPipeline so it doesn't reload
    or rebuild embeddings every time.
    """
    return FactCheckPipeline()

# Initialize the pipeline
pipeline = load_pipeline()

# UI title
st.title("Fact Checker 🚀")

# Claim input box
claim = st.text_area(
    "Enter your claim:",
    height=140,
    placeholder="e.g. India achieved record food grain output in 2025."
)

# Check Fact button
if st.button("Check Fact"):
    if not claim.strip():
        st.warning("Please enter a claim.")
    else:
        with st.spinner("Checking..."):
            result = pipeline.run(claim)

        # Show claim
        st.subheader("Claim")
        st.write(claim)

        # Evidence
        st.subheader("Evidence (Top Matches)")
        for ev in result.get("evidence", []):
            st.write("- " + ev)

        # Verdict
        st.subheader("Verdict")
        st.write(result.get("verdict", "No verdict"))

        # Reasoning
        st.subheader("Reasoning")
        st.write(result.get("reasoning", "No reasoning generated."))

        # Raw JSON
        st.subheader("Raw JSON Output")
        st.json(result)
