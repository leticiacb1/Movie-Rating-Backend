from fastapi import APIRouter
from backend.models.base_models import Avaliacao , Filme
from fastapi import status
import json

from ..services.utils_filmes import create_film  , get_film

router = APIRouter()

@router.get("/filmes/")
async def show_filmes():

    result = get_film()
    return {"status_code": 200 , "filmes" : result}

@router.post("/filmes/")
async def cadastra_filmes(film: Filme):

    result = create_film(film)
    return {"status_code": 201 }  