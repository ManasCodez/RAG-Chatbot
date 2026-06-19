from langchain_ollama import OllamaEmbeddings

# for qureies
def embed(query):
    embeddings = OllamaEmbeddings(model='nomic-embed-text')
    
    embed = embeddings.embed_query(query)

    return embed
