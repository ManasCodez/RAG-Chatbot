from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

def get_vectorstore():

    embedding = OllamaEmbeddings(model ='nomic-embed-text')
    embedding.embed_query('test')

    return  Chroma(
        collection_name="Files",
        embedding_function=OllamaEmbeddings(
            model="nomic-embed-text"
        ),
        persist_directory="./data/chroma/vector_database",
    )
    



def get_uploaded_files(vectorstore):

    data = vectorstore.get()

    files = set()

    for meta in data["metadatas"]:
        files.add(meta["filename"])

    return sorted(list(files))