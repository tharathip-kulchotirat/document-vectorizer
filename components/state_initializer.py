import streamlit as st

def state_initializer():
    if 'document_vectorizer_page' not in st.session_state:
        st.session_state['document_vectorizer_page'] = False
    if 'OPENAI_API_KEY' not in st.session_state:
        st.session_state['OPENAI_API_KEY'] = None
    if 'submit_api_key' not in st.session_state:
        st.session_state['submit_api_key'] = False
    if 'start_vectorization' not in st.session_state:
        st.session_state['start_vectorization'] = False
    if 'vectorized_index' not in st.session_state:
        st.session_state['vectorized_index'] = False