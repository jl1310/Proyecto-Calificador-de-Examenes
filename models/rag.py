from llama_index import SimpleDirectoryReader, VectorStoreIndex

def build_index(directory):
    documents = SimpleDirectoryReader(directory).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index