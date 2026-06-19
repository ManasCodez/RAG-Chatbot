# RAG Chatbot

A local Retrieval-Augmented Generation (RAG) chatbot built using:

- Streamlit
- LangChain
- ChromaDB
- Ollama
- Qwen
- Nomic Embed Text

Users can upload PDF, TXT and DOCX files and chat with their documents locally.

---

# Features

- Multi-file upload
- PDF, TXT and DOCX support
- Chroma Vector Database
- Local embeddings using Nomic Embed Text
- Local LLM inference using Ollama
- Streaming responses
- Document selection and filtering
- Document deletion
- Adjustable model settings

---

# Project Structure

```text
RAG-CHATBOT/
│
├── data/
│
├── rag/
│   ├── chunker.py
│   ├── ingest.py
│   ├── llm.py
│   ├── retriever.py
│   └── vectorstore.py
│
├── .gitignore
├── main.py
└── requirements.txt
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/ManasCodez/RAG-Chatbot

cd RAG-CHATBOT
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip3 install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

## 5. Download Required Models

### Qwen 3

```bash
ollama pull qwen3:8b
```

### Nomic Embed Text

```bash
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

Expected output:

```text
qwen3:8b
nomic-embed-text
```

---

## 6. Run the Application

```bash
streamlit run main.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# Usage

## Upload Documents

1. Upload one or more PDF, TXT or DOCX files.
2. Click **Process Files**.
3. Wait for ingestion and embedding generation.

---

## Ask Questions

Example prompts:

```text
Summarize the uploaded resume.
```

```text
What skills are mentioned in the document?
```

```text
What projects has the candidate completed?
```

---

## Manage Documents

- Enable/disable documents using checkboxes.
- Delete documents using the ❌ button.
- Only selected documents are searched during retrieval.

---

# Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama
- Qwen3
- Nomic Embed Text

---

# Author

Manas Sharma

GitHub:
https://github.com/ManasCodez