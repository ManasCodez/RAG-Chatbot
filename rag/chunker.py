from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk(docs):
    spliiter = RecursiveCharacterTextSplitter(chunk_size=800,
                                              chunk_overlap= 200)
    
    docs = spliiter.split_documents(docs)

    return docs
