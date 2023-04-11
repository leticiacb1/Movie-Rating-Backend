from fastapi import APIRouter
from backend.models.base_models import Avaliacao
from fastapi import status
import json

from ..services.utils_avaliacoes import get_all_rating , create_rating, delete_rating, get_rating

router = APIRouter()

@router.get("/avaliacoes/")
async def get_all_avaliacoes():
    result = get_all_rating()
    return {"status_code": 200 , "avaliacoes" : result}

@router.get("/avaliacoes/{id}")
async def get_avaliacao_id(id: int):
    result = get_rating(id)
    return {"status_code": 200 , "avaliacao" : result}

@router.post("/avaliacoes/")
async def cadastra_avaliacao(rate: Avaliacao):
    result = create_rating(rate)
    return {"status_code": 201 }  

@router.delete("/avaliacoes/{id}")
async def deleta_avaliacao(id: int):
    result = delete_rating(id)
    return {"status_code": 200 } 