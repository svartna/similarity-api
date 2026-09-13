from fastapi import FastAPI
from models import SimilarityRequest
from similarity import compute_similarity

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/similarity")
def get_similarity(request: SimilarityRequest):
    ids, similarity_matrix = compute_similarity(request.items)
    return {
        "ids": ids,
        "similarity_matrix": similarity_matrix.tolist()
    }
