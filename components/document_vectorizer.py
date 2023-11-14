import streamlit as st
from .example_use import example_code
from .utils.index_utils import build_index, save_file, export_index

def document_vectorizer_page():
    col1, col2 = st.columns(2)
    with col1:
        files = st.file_uploader("Document You Want To Vectorize.",  accept_multiple_files=False, type="pdf")
        submit = st.button("Start Vectorization", type="primary")
        
    
    st.markdown("---")
    export_placeholder = st.empty()
    example_placeholder = st.empty()
            
    with col2:
        st.markdown("Tester")

    if submit:
        st.session_state.start_vectorization = True
        
    if st.session_state.start_vectorization:
        if files:
            path = save_file(files)
            
            with col2:
                with st.spinner("Vectorizing Documents, Please wait."):
                    index, engine = build_index(path)
                    st.session_state.vectorized_index = True
                    
                if st.session_state.vectorized_index:
                    user_text = st.text_input("Message: ")
                    result = engine.query("What is this document about?")
                    if user_text:
                        result = engine.query(user_text)
                        
                    st.write(result)
                    
                    path = export_index(index)
                        
                    with open(path, "rb") as f:
                        export_placeholder.download_button(
                            label="Download Your Index",
                            data=f,
                            file_name="your_index.zip",
                            mime="application/zip",
                            key="downloaded"
                        )
                        example_code(example_placeholder)
                            
        else:
            with col2:
                st.warning("Please upload documents to vectorize.")
            