# 🔍 LLM Fact-Checking System  
### 🧠 Machine Learning Engineer – LLM Task Assignment

A lightweight **LLM-powered Fact Verification System** that extracts claims, retrieves factual evidence, and classifies each claim as **True**, **False**, or **Unverifiable** using a Retrieval-Augmented Generation (RAG) pipeline.

This project is built as per the task instructions from:  
📄 *Machine Learning Engineer – LLM Task Assignment* (provided in the challenge)

---

# 🌟 Features

- ✂️ **Automatic Claim Extraction** using NLP  
- 📚 **Trusted Fact Base** ingestion (CSV → chunks → embeddings)  
- 🔍 **Top-K Retrieval** using FAISS / Chroma  
- 🤖 **LLM-based Comparison** with structured JSON outputs  
- ⚡ Deterministic prompt (temperature = 0) for accuracy  
- 🖥️ **Streamlit UI** for interactive fact-checking  
- 🧪 Testable pipeline (E2E claim → retrieval → verdict)

---

# 🛠️ Tech Stack

| Layer | Tools |
|------|-------|
| **Language** | Python 🐍 |
| **NLP** | spaCy, Transformers |
| **Embeddings** | Sentence-Transformers |
| **Vector DB** | FAISS / Chroma |
| **LLM** | OpenAI GPT-4o / GPT-4o-mini (configurable) |
| **UI** | Streamlit |
| **Data** | Custom facts.csv (trusted dataset) |

---

# 📂 Project Structure

```
llm-fact-checker/
│
├── data/
│   ├── facts.csv
│   ├── faiss.index
│   └── meta.pkl
│
├── src/
│   ├── ingest.py
│   ├── nlp.py
│   ├── retriever.py
│   ├── llm_compare.py
│   ├── pipeline.py
│   └── app.py
│
├── notebooks/
│   └── demo.ipynb
│
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Create Virtual Environment
```bash
conda create -n llmFactChecker python
```

---

## 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## 3️⃣ Build Vector Index (Embeddings)
```bash
python src/ingest.py
```
This generates:

- `data/faiss.index`  
- `data/meta.pkl`

---

## 4️⃣ Run the Fact-Checking App (Streamlit)
```bash
streamlit run src/app.py
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
