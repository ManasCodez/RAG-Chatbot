from langchain_ollama import OllamaEmbeddings

# for qureies
def embed(query):
    embeddings = OllamaEmbeddings(model='hi')
    
    embed = embeddings.embed_query(query)

    return embed
