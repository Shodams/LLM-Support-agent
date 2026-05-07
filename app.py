"""
Streamlit UI for chatbot
"""

import streamlit as st

from app.rag_pipeline import load_rag_pipeline

st.set_page_config(page_title="LLM Support Agent")

st.title("💬 LLM Support Agent")

# Load pipeline once
@st.cache_resource
def get_pipeline():
    return load_rag_pipeline()

qa_chain = get_pipeline()

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        response = qa_chain.run(query)
        st.write(response)
