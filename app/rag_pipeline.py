"""
RAG Pipeline:
- Loads FAISS index
- Retrieves relevant documents
- Queries LLM
"""

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

from app.config import EMBEDDING_MODEL, VECTOR_DB_PATH, OPENAI_API_KEY


def load_rag_pipeline():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    vectorstore = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=OPENAI_API_KEY
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa_chain
