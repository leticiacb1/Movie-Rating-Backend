from fastapi import APIRouter
from backend.models.base_models import Filme
from fastapi import status
import json

from ..services.utils_filmes import create_film , get_all_films , update_film , delete_film , get_film

router = APIRouter()

@router.get("/filmes/")
async def get_all_filmes():
    result = get_all_films()
    return {"status_code": 200 , "filmes" : result}

@router.get("/filmes/{id}")
async def get_filme_id(id: int):
    result = get_film(id)
    return {"status_code": 200 , "filme" : result}

@router.post("/filmes/")
async def cadastra_filmes(film: Filme):
    result = create_film(film)
    return {"status_code": 201 }  

@router.put("/filmes/{id}/")
async def update_filme(id: int , film: Filme):
    result = update_film(id , film.dict())
    return {"status_code": 200 } 

@router.delete("/filmes/{id}")
async def deleta_filme(id: int):
    result = delete_film(id)
    return {"status_code": 200 } 