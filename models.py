from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

class Item(BaseModel):
    id: str
    features: Dict[str, float]

class SimilarityRequest(BaseModel):
    items: List[Item]
