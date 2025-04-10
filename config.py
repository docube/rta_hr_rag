### config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "../data/uploads")
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "../faiss_index/index.faiss")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"