from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk(docs, chunk_size, chunk_overlap):
    spliiter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                              chunk_overlap= chunk_overlap)
    
    docs = spliiter.split_documents(docs)

    return docs
