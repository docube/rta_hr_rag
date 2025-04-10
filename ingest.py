### ingest.py

import os
from config import UPLOAD_DIR, EMBEDDING_MODEL_NAME
from utils import load_file
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def ingest_files():
    texts, metadata = [], []
    for filename in os.listdir(UPLOAD_DIR):
        filepath = os.path.join(UPLOAD_DIR, filename)
        try:
            content = load_file(filepath)
            chunks = [content[i:i+500] for i in range(0, len(content), 500)]
            texts.extend(chunks)
            metadata.extend([{"filename": filename}] * len(chunks))
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
    embeddings = model.encode(texts)
    return embeddings, texts, metadata