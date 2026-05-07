# LLM Support Agent (RAG + LangChain + FAISS)

An AI-powered customer support chatbot built using Retrieval-Augmented Generation (RAG), LangChain, and FAISS.  
It retrieves relevant knowledge from a dataset and generates accurate, context-aware responses using LLMs.

## Demo

![App Screenshot](assets/demo.png)


## Problem

Traditional chatbots rely on static rules or limited context.

This project solves:
- Lack of contextual responses
- Poor knowledge retrieval
- Scalability issues in support systems

## 💡 Solution

This project uses a RAG pipeline:
- Converts data into embeddings
- Stores in FAISS vector DB
- Retrieves relevant context
- Uses LLM to generate answers

  
# LLM Support Agent (RAG + Tools)

A production-ready LLM application demonstrating:

- Retrieval-Augmented Generation (RAG)
- Vector databases (FAISS)
- Prompt-based reasoning
- Tool-augmented agents
- Streamlit UI



## Features

- Custom dataset generation
- Local vector search (FAISS)
- Lightweight embeddings
- OpenAI-powered responses
- Extensible agent system

---

## Architecture

User Query → Embeddings → FAISS → Retrieved Context → LLM → Response




## 📂 Project Structure

app/
 ├── data_generator.py
 ├── ingest.py
 ├── rag_pipeline.py
 ├── config.py
 ├── agent.py

vector_store/
data/
app.py
---
## Future Improvements

- Add chat memory
- Support PDF ingestion
- Deploy to cloud (Streamlit / AWS)
- Add multi-agent system

## ▶️ Run Locally

```bash
git clone https://github.com/Shodams/LLM-Support-agent
cd LLM-Support-agent

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python -m app.data_generator
python -m app.ingest
streamlit run app.py




