from fastapi import APIRouter
from backend.models.base_models import Filme
from fastapi import status
import json

from ..services.utils_filmes import create_film , get_all_films , update_film , delete_film , get_film

router = APIRouter()

@router.get("/filmes/" , summary="Retorna todos os filmes da base de dados")
async def get_all_filmes():

    """
    Cria um filme com as seguintes informações

    - **name**: Título do filme
    - **description** : breve sinopse do filme
    - **release_year** : ano de lançamento do filme
    - **length** : duração do filme em minutos
    
    """

    result = get_all_films()
    return {"status_code": 200 , "filmes" : result}

@router.get("/filmes/{id}")
async def get_filme_id(id: int):
    result = get_film(id)
    return {"status_code": 200 , "filme" : result}

@router.post("/filmes/")
async def cadastra_filmes(film: Filme):
    result = create_film(film)

    if(result == "OK"):
        return {"status_code": 201 }  
    else:
        return {"status_code": 404 , "mensagem":result }  

@router.put("/filmes/{id}/")
async def update_filme(id: int , film: Filme):
    result = update_film(id , film.dict())

    if(result == "OK"):
        return {"status_code": 200 } 
    else:
        return {"status_code": 404 , "mensagem":result }

@router.delete("/filmes/{id}")
async def deleta_filme(id: int):
    result = delete_film(id)
    return {"status_code": 200 } 