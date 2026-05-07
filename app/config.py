import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Embedding model (lightweight for your machine)
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Vector store path
VECTOR_DB_PATH = "vector_store"
