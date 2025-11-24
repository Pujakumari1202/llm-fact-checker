import os

# Project root
project_name = "llm-fact-checker"

# Updated folder structure
folders = [
    f"{project_name}/data",
    f"{project_name}/src",
    f"{project_name}/llmfact",
    f"{project_name}/chroma_db",   # chroma persistent DB
]

# Updated file structure
files = {
    f"{project_name}/README.md": "# LLM Fact-Checker (ChromaDB + HuggingFace)\n",
    f"{project_name}/requirements.txt": "",
    f"{project_name}/data/facts.csv": "id,source_url,source_date,statement,plain_text\n",

    # src files
    f"{project_name}/src/embedder.py": "",
    f"{project_name}/src/retriever.py": "",
    f"{project_name}/src/llm_compare.py": "",
    f"{project_name}/src/pipeline.py": "",
    f"{project_name}/src/__init__.py": "",

    # Streamlit UI
    f"{project_name}/llmfact/app.py": "",

    # env (HuggingFace key)
    f"{project_name}/.env": "HF_API_KEY=\nHF_MODEL=mistralai/Mistral-7B-Instruct\n",
}

# Create folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"[+] Created folder: {folder}")
    else:
        print(f"[!] Folder already exists, skipped: {folder}")

# Create files
for filepath, content in files.items():
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Created file: {filepath}")
    else:
        print(f"[!] File already exists, skipped: {filepath}")

print("\n🎉 Project setup complete! Existing files/folders were not changed.")
