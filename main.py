import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    AIMessage
)
import subprocess

from rag.ingest import ingestpdf
from rag.chunker import chunk
from rag.retriever import retriever
from rag.vectorstore import get_vectorstore, get_uploaded_files
from rag.llm import get_model

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []




#check if ollama is running 


try:
    subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True,
        check=True
)

except Exception:
    st.error("Ollama is not running.")
    st.warning("Make sure Ollama app is installed and Running")
    st.markdown("**Start Ollama with:**")
    st.code("ollama serve")

    st.stop()




try:
    vectorstore = get_vectorstore()
except Exception as e:
    st.warning("Make sure nomic-text-embed is install")
    st.markdown("In terminal run: ")
    st.code("ollama pull nomic-embed-text")
    st.stop()



stored_files = get_uploaded_files(vectorstore)



# Page Title
st.title("LOCAL RAG Chatbot")
st.markdown("""

    ## 👋 Welcome to RAG Chatbot

    Upload your documents and ask questions about them.

    ### Features

    - 📄 PDF, DOCX, TXT Support

    - 🔍 Semantic Search

    - 🤖 Multiple Ollama Models

    - 💾 Local Vector Database

    - 🔒 Fully Local Processing

    """)



# Sidebar Upload Section


st.sidebar.header("Upload Documents")

files = st.sidebar.file_uploader(
    "Upload Files",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

chunk_size = st.sidebar.slider("Chunk Size",1,1000,500, help="Size of each chunk")
chunk_overlap = st.sidebar.slider("Chunk Overlap", 1, 500,200, help="Overlapping between two chunks")

# Process button
if st.sidebar.button("Process Files"):
    if files:

        for file in files:

            if file.name not in stored_files:

                docs = ingestpdf(file)
                
                docs_chunk = chunk(docs,chunk_size,chunk_overlap)
                vectorstore.add_documents(docs_chunk)
                st.rerun()


        st.sidebar.success( "Files processed successfully!")

    else:
        st.sidebar.warning("Please upload files first.")




# Document Management




st.sidebar.markdown("---")
st.sidebar.subheader("Documents")



active_files = []

for filename in stored_files:

    col1, col2 = st.sidebar.columns([4, 1])

    with col1:

        checked = st.checkbox(
            filename,
            value=True,
            key=f"active_{filename}"
        )
        if checked:
            active_files.append(filename)


    with col2:
        if st.button("❌",key=f"delete_{filename}"):

            vectorstore.delete(
            where={
                "filename": filename
            }
            )

            st.rerun()


llm_options = ['qwen3:8b','llama3.2:3b','gemma3:4b','deepseek-r1:1.5b',"deepseek-r1:7b","mistral:7b","gpt-oss:20b","tinyllama:1.1b"]

llm = st.sidebar.selectbox("Select Your Model",llm_options,help="Select model according to your device")
temperature = st.sidebar.slider("Temperrature", 0.0,1.0,0.2,help="Higher values make responses more creative.")
reasoning = st.sidebar.checkbox("Reasoning",value=False, help="More accurate answers but take more time")
max_token = st.sidebar.slider("Max output Tokens",1,2000,1000, help="Maximun length of Genarated output")
Top_k_chunks = st.sidebar.number_input("Top K chunks",1,200,10, help="Number of chunks to be retrived")

# Model
try:
    model = get_model(
        llm,
        reasoning,
        max_token,
        temperature
    )

except Exception as e:

    st.warning(f"Model not available: {e}")

    st.markdown("Make sure Ollama is downloaded "
        "[Download Ollama](https://ollama.com/download)")
    
    st.markdown(f"Then in terminal run: ")
    st.code(f"ollama pull {llm}")

    st.stop()

# Chat History


for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)


# ----------------------------
# Chat Input
# ----------------------------

prompt = st.chat_input(
    "Enter Your Thoughts"
)


if prompt:

    # User Message
    with st.chat_message("user"):

        st.markdown(prompt)

        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

    
    if not active_files:
        st.warning("Please select at least one document.")
        


    retrieved_result = retriever(prompt, active_files,Top_k_chunks)

    context = "\n\n".join(doc.page_content for doc in retrieved_result)


    st.sidebar.write("Retrieved Chunks: ", len(retrieved_result))
    st.sidebar.write("total Number of Chunks: ",len(vectorstore.get()['ids']))
    messages = [
        SystemMessage(
    content=f"""
You are a helpful retrieveal augmented generation assistant.

Use ONLY the provided context.

If the answer is not contained in the context,
reply:

"I could not find that information in the uploaded documents."

Do not make up information.
and if the user is saying something related to the file, or book, he is referring to the text from the context

Context:
{context}
"""
),
    HumanMessage(content=prompt)
]

    

    # Assistant Message
    with st.chat_message("assistant"):

        def stream_response():

            for chunk in model.stream(messages):
                yield chunk.content

        response = st.write_stream(
            stream_response()
        )

        st.session_state.messages.append(
            AIMessage(content=response)
        )