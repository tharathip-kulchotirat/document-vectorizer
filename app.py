import streamlit as st
import os
from components.state_initializer import state_initializer
from components.document_vectorizer import document_vectorizer_page

st.set_page_config(page_title="Invitrace Document Vectorizer")

state_initializer()
# Title
st.title(":blue[Invitrace Document Vectorizer]")

# User API key
api_key = st.text_input("OpenAI API Key: ")
submit = st.button("Submit API Key")

# session management
if submit:
    st.session_state.submit_api_key = True
# session management

if st.session_state.submit_api_key:
    st.session_state["OPENAI_API_KEY"] = api_key
    st.session_state.submit_api_key = False

if st.session_state.OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = st.session_state.OPENAI_API_KEY
    try: 
        from llama_index import GPTVectorStoreIndex, Document
        vector_store = GPTVectorStoreIndex.from_documents([Document("Test")])
        st.success("API Key already Set: " + st.session_state.OPENAI_API_KEY + " | MAKE SURE that your API KEY is correct!")
        st.session_state.document_vectorizer_page = True
    except Exception as e:
        st.error("API Key is not valid. Please provide a valid API Key.")
else:
    st.warning("Please provide correct API key. Don't have one? Get one here: https://platform.openai.com/signup?launch")
    
if st.session_state.document_vectorizer_page:
    document_vectorizer_page()