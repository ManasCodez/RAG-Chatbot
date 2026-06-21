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

<img width="2048" height="1128" alt="1" src="https://github.com/user-attachments/assets/3155e6cd-2d1b-4017-ac08-1652edcbd9cd" />
<img width="2048" height="1128" alt="2" src="https://github.com/user-attachments/assets/19604117-3d5a-4b52-8f26-192eafe6a3cb" />
<img width="2048" height="1128" alt="3" src="https://github.com/user-attachments/assets/506d55aa-f81c-4e07-990a-6a8f1a3c9a7f" />
<img width="2048" height="1128" alt="4" src="https://github.com/user-attachments/assets/e55ff9bc-aa49-4250-a8a0-b75964ed8a85" />
<img width="2048" height="1128" alt="5" src="https://github.com/user-attachments/assets/27560b52-1fae-413d-9186-55018575f04e" />






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
