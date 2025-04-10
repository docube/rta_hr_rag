### main.py

from fastapi import FastAPI, UploadFile, File, Form
from ingest import ingest_files
from vector_store import save_faiss_index, load_faiss_index, search_index
from query_engine import get_mock_response, embed_query
import os
from config import UPLOAD_DIR

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())
    return {"status": "uploaded", "filename": file.filename}

@app.post("/ingest")
def ingest():
    embeddings, texts, metadata = ingest_files()
    save_faiss_index(embeddings)
    return {"status": "ingested", "chunks": len(texts)}

@app.get("/query")
def query_system(q: str):
    index = load_faiss_index()
    query_vector = embed_query(q)
    results = search_index(index, query_vector, k=3)
    response = get_mock_response(q)
    return {"response": response, "matched_indexes": results.tolist()}