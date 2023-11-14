import streamlit as st

def example_code(component):
    component.code("""
            # USAGE EXAMPLE
            from load_local_index import load_index
            
            path = "./index"
            index, retriever, engine = load_index(path)
            
            # to query your document
            engine.query("What is this document about?")
            
            # to retrieve source where the query engine use
            retriever.retrieve("What is this document about?")
            
            """, language="python")
