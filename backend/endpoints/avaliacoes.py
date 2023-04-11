from fastapi import APIRouter
from backend.models.base_models import Avaliacao
from fastapi import status
import json

from ..services.utils_avaliacoes import get_all_rating , create_rating

router = APIRouter()

@router.get("/avaliacoes/")
async def get_all_avaliacoes():
    result = get_all_rating()
    return {"status_code": 200 , "avaliacoes" : result}

@router.post("/avaliacoes/")
async def cadastra_avaliacao(rate: Avaliacao):
    result = create_rating(rate)
    return {"status_code": 201 }  