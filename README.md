# 🔍 LLM Fact-Checking System  
### 🧠 Machine Learning Engineer – LLM Task Assignment

A lightweight **LLM-powered Fact Verification System** that takes a claim, retrieves factual evidence, and classifies it as **Likely True**, **Likely False**, or **Unverifiable** using a Retrieval-Augmented Generation (RAG) pipeline.

This project was built for the task described in the provided assignment PDF:  
`file:///mnt/data/Machine Learning Engineer – LLM Task Assignment.pdf`

---

## 🌟 Features

- 📝 Simple claim input (user-provided)
- 📚 Trusted fact base ingestion (`data/facts.csv`)
- 🔍 Semantic Top-K retrieval using **ChromaDB**
- 🧠 Sentence embeddings via `all-MiniLM-L6-v2`
- 🤖 LLM reasoning & classification via HuggingFace Inference API
- 📦 Structured JSON output: `{ "verdict", "evidence", "reasoning" }`
- 🖥️ Streamlit UI for interactive checks

---


# 🛠️ Tech Stack

| Layer | Tools |
|-------|--------|
| **Language** | Python 🐍 |
| **NLP** | spaCy (en_core_web_sm) |
| **Embeddings** | Sentence-Transformers (all-MiniLM-L6-v2) |
| **Vector DB** | ChromaDB |
| **LLM (API)** | HuggingFace Inference API (Mistral-7B-Instruct or any free model) |
| **UI** | Streamlit |
| **Dataset** | Custom `facts.csv` (trusted fact base) |
| **Environment** | Conda + `.env` secrets |
| **Utilities** | pandas, numpy, tqdm |


---


# 📂 Project Structure

```
llm-fact-checker/
│
├── llmfact/
│   └── app.py
│
├── src/
│   ├── embedder.py
│   ├── retriever.py
│   ├── llm_compare.py
│   ├── pipeline.py
│   └── __init__.py
│
├── data/
│   └── facts.csv
│
│
├── .env
├── README.md
└── requirements.txt

```

---

# 🚀 Getting Started

## 1️⃣ Create Virtual Environment
```bash
conda create -n llmFactChecker python=3.10 -y


```

---

## 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---


## 3 Run the Fact-Checking App (Streamlit)
```bash
streamlit run app.py

```

Open in browser → **http://localhost:8501**

---

# 🧠 Pipeline Workflow

### **1. Claim Extraction**
- Uses spaCy  
- Extracts meaningful, verifiable sentences

### **2. Embedding + Retrieval**
- Embeds claims using `all-MiniLM-L6-v2`  
- Retrieves the top-K closest factual statements

### **3. LLM Comparison**
LLM receives:
- Claim  
- Retrieved Evidence  
- JSON-only instructions  

Returns:
```json
{
  "verdict": "True | False | Unverifiable",
  "evidence": [...],
  "reasoning": "Short explanation"
}
```

### **4. Streamlit UI**
- Paste text → get structured verdicts  
- Supports multiple claims  
- Displays:
  - Verdict  
  - Matched Evidence  
  - Reasoning

---

# 🧪 Testing the System

Use the notebook:
```
notebooks/demo.ipynb
```

Test categories:
- ✔ True claims  
- ❌ False claims  
- 🤷 Unverifiable claims  
- 🔁 Retrieval boundary tests  

---

# 📦 Deliverables (As Required)

- 🗂️ Python code (.py + notebook)  
- 📝 README.md  
- 📊 Sample test data (input + output)  
- 🎥 5–7 min Video walkthrough  
- 🧪 Example prompts and results  
- 📁 Zip file or GitHub link  

---

# ⚠️ Limitations

- ❗ Performance depends on size/quality of **facts.csv**  
- ❗ LLM can hallucinate → mitigated using strict prompts  
- ❗ Retrieval errors may mislead the LLM  

---

# 🚀 Future Improvements

- 🔄 Better Claim Classification Model (fine-tuned)  
- 🧮 Date Reasoning (temporal matching)  
- 🏛️ Larger fact database (Gov sources / verified news)  
- 🤖 Local LLM (Mistral / Llama-3) support  
- 📈 Add confidence scores  

---

# 👩‍💻 Author

**Puja Kumari**  
AI/ML Engineer | LLM Developer | Generative AI  
📧 Email: **puja02538@gmail.com**  
🌐 GitHub: **github.com/Pujakumari1202**

---

# 📜 License
MIT License

---

If you want, I can also generate:

✅ **Colorful Badges**  
✅ **Project Banner Image**  
✅ Full **src/ folder code files**  
✅ A sample **facts.csv (30 entries)**  
Just tell me!
