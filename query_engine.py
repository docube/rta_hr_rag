### query_engine.py

from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL_NAME
import numpy as np

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def get_mock_response(query):
    return f"🔍 You asked: '{query}'. [Mocked answer here from HR data]"

def embed_query(query):
    return model.encode([query])