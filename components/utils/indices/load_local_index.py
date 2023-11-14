from llama_index import StorageContext, load_index_from_storage

def load_index(path):
    storage_context = StorageContext.from_defaults(persist_dir=path)
    loaded_index = load_index_from_storage(storage_context)
    retriever = loaded_index.as_retriever()
    query_engine = loaded_index.as_query_engine(response_mode='compact')
    
    return loaded_index, retriever, query_engine