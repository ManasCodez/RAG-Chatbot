import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    AIMessage
)
from rag.ingest import ingestpdf
from rag.chunker import chunk
from rag.retriever import retriever
from rag.vectorstore import get_vectorstore, get_uploaded_files


# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []



# Models


model = ChatOllama(
    model="qwen3:8b",
    reasoning=False,
    num_predict=1000
)


vectorstore = get_vectorstore()

stored_files = get_uploaded_files(vectorstore)



# Page Title
st.title("RAG Chatbot")



# Sidebar Upload Section


st.sidebar.header("Upload Documents")

files = st.sidebar.file_uploader(
    "Upload Files",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

# Process button
if st.sidebar.button("Process Files"):
    if files:

        for file in files:

            if file.name not in stored_files:

                docs = ingestpdf(file)
                
                docs_chunk = chunk(docs)
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
        


    retrieved_result = retriever(prompt, active_files=active_files)

    context = "\n\n".join(doc.page_content for doc in retrieved_result)


    st.sidebar.write("Retrieved results: ", len(retrieved_result))
    st.sidebar.write("total Number of Chunks: ",len(vectorstore.get()['ids']))
    messages = [
        SystemMessage(
    content=f"""
You are a helpful RAG assistant.

Use ONLY the provided context.

If the answer is not contained in the context,
reply:

"I could not find that information in the uploaded documents."

Do not make up information.

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