# 📄 SmartDoc AI – RAG-based PDF Chatbot

## 🚀 Overview

SmartDoc AI is a **Retrieval-Augmented Generation (RAG)** based chatbot that allows users to upload PDF documents and interact with them conversationally.

It uses **semantic search + local LLM** to provide accurate, context-aware answers without relying on external APIs.

---

## ✨ Features

* 📄 Upload and process multiple PDF documents
* 🔍 Semantic search using embeddings
* 🤖 ChatGPT-style conversational interface
* 💬 Multi-turn chat history (session-based memory)
* ⚡ Local LLM (no API cost)
* 📚 Source context display for transparency

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **LLM:** FLAN-T5 (local model via Transformers)
* **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **Vector Database:** FAISS
* **Framework:** LangChain

---

## ⚙️ How It Works

1. Upload PDF documents
2. Extract text using PDF loader
3. Split text into smaller chunks
4. Convert chunks into embeddings
5. Store embeddings in FAISS vector database
6. User query is converted into embedding
7. Retrieve top relevant chunks
8. Pass context + query to LLM
9. Generate accurate answer

---

## 📁 Project Structure

```
SmartDoc-AI/
│
├── app.py                # Main Streamlit app
├── requirements.txt     # Dependencies
├── data/                # Uploaded PDFs (auto-created)
└── README.md            # Project documentation
```

---

## 🛠️ Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/SmartDoc-AI.git
cd SmartDoc-AI
```

### 2. Create Virtual Environment

```
python -m venv rag_env
```

Activate:

* Windows:

```
rag_env\Scripts\activate
```

* Mac/Linux:

```
source rag_env/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the App

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📌 Example Use Cases

* 📚 Study assistant (ask questions from notes)
* 🏢 Business document analysis
* ⚖️ Legal document QA
* 🏥 Medical report understanding
* 🚗 Insurance policy validation

---

## 🚧 Limitations

* Local model may be slower than API-based models
* Context length is limited by chunking
* No long-term memory (session-based only)

---

## 🚀 Future Improvements

* ✅ Conversational memory (context-aware chat)
* ⚡ Faster & better models (Mistral / LLaMA)
* 🌐 Deployment (Render / HuggingFace Spaces)
* 📄 Highlight answers in PDF
* 🔍 Hybrid search (keyword + vector)

---

## 💡 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Embeddings & Semantic Search
* Vector Databases (FAISS)
* Transformer-based LLMs
* Chunking & Context Injection

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Hugging Face Transformers
* LangChain
* FAISS
* Streamlit

---

## 👨‍💻 Author

**Dharun**
AI/ML Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
