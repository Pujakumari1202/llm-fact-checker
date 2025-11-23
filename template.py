import os

# Project Root Name

project_name = "llm-fact-checker"


# Folder Structure

folders = [
    f"{project_name}/data",
    f"{project_name}/src",
    f"{project_name}/notebooks",
]

files = {
    f"{project_name}/README.md": "# LLM Fact-Checking System\n",
    f"{project_name}/requirements.txt": "",
    f"{project_name}/data/facts.csv": "id,source_url,source_date,statement,plain_text\n",
    f"{project_name}/notebooks/demo.ipynb": "",
    f"{project_name}/src/__init__.py": "",
    f"{project_name}/src/ingest.py": "",
    f"{project_name}/src/nlp.py": "",
    f"{project_name}/src/retriever.py": "",
    f"{project_name}/src/llm_compare.py": "",
    f"{project_name}/src/pipeline.py": "",
    f"{project_name}/src/app.py": "",
    f"{project_name}/.env": "OPENAI_API_KEY=\n",
}


# Create Folders (Skip if Exists)

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"[+] Created folder: {folder}")
    else:
        print(f"[!] Folder already exists, skipped: {folder}")


# Create Files (Skip if Exists)

for filepath, content in files.items():
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Created file: {filepath}")
    else:
        print(f"[!] File already exists, skipped: {filepath}")

print("\n🎉 Project setup complete! Existing files/folders were not changed.")
