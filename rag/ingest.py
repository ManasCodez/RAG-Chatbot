from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
import streamlit as st
import tempfile
from pathlib import Path

def ingestpdf(uploaded_file):
    if uploaded_file is None:
        return []
    with tempfile.NamedTemporaryFile(delete=False,
                                     suffix=Path(uploaded_file.name).suffix) as tmp:
            tmp.write(uploaded_file.getvalue())
            temp_path = Path(tmp.name)
       
        

    
    ext = temp_path.suffix.lower()

    
    if ext == ".pdf":
            loader = PyPDFLoader(str(temp_path))
    elif ext == ".txt":
            loader = TextLoader(str(temp_path), encoding="utf-8")
    elif ext == ".docx":
            loader = Docx2txtLoader(str(temp_path))
    else:
            raise ValueError(f"Encountered unexpected document processing formatexception extension: {ext}")
            
    docs = loader.load()
    # Cleanly map standard source string metadata references
    for doc in docs:
            doc.metadata["filename"] = uploaded_file.name
            if "page" not in doc.metadata:
                doc.metadata["page"] = 1
    return docs
    
    