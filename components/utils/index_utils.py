from llama_index import GPTVectorStoreIndex, download_loader
import shutil
import os.path
import streamlit as st
from pathlib import Path

def save_file(file):
    file_path = Path("components/utils/temp", file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

@st.cache_resource
def build_index(file_path):
    reader = download_loader("PDFReader")
    loader = reader()
    documents = loader.load_data(file_path)
    
    index = GPTVectorStoreIndex.from_documents(documents=documents)
    query_engine = index.as_query_engine(response_mode='compact')
    
    return index, query_engine
    
def export_index(index):
    index_path = "components/utils/indices/index"
    directory_to_be_zipped = "components/utils/indices"
    save_path = 'components/utils/indices'
    index.storage_context.persist(persist_dir=index_path)
    
    # prepare zip
    shutil.make_archive(save_path, 'zip', directory_to_be_zipped)
    
    if os.path.exists(save_path + ".zip"):
        return save_path + ".zip"
    else: 
        return None
    
    