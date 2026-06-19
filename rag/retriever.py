from rag.vectorstore import get_vectorstore
import streamlit as st

def retriever(query, active_files,k):
    if not active_files:
        return []
    
    vectorstore = get_vectorstore()
    

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": k,
            "filter": {
                "filename": {
                    "$in": active_files
                }
            }
        }
    )

    return retriever.invoke(query)