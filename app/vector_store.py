### vector_store.py

import faiss
import numpy as np
from config import FAISS_INDEX_PATH

def save_faiss_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    faiss.write_index(index, FAISS_INDEX_PATH)

def load_faiss_index():
    return faiss.read_index(FAISS_INDEX_PATH)

def search_index(index, query_vector, k=5):
    D, I = index.search(query_vector, k)
    return I