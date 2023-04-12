from fastapi import APIRouter
from backend.models.base_models import Filme
from fastapi import status
import json

from ..services.utils_filmes import create_film , get_all_films , update_film , delete_film , get_film

router = APIRouter()

@router.get("/filmes/" , summary="Retorna todos os filmes da base de dados")
async def get_all_filmes():

    """
    Retorna as informações de todos os filmes da base no formato:

    **filme_id** : {\\
            name : "Titanic",\\
            description : " Um filme que mistura um jovem romance com uma infeliz tragédia.",\\
            release_year 1998,\\
            length : 125\\
    }

    """

    result = get_all_films()
    return {"status_code": 200 , "filmes" : result}

@router.get("/filmes/{id}" , summary="Retorna filme do id especificado")
async def get_filme_id(id: int):

    """
    Retorna as informação do filme com o respectivo {id}, no formato:

    **filme_id** : {\\
        name : "Titanic",\\
        description : " Um filme que mistura um jovem romance com uma infeliz tragédia.",\\
        release_year: 1998,\\
        length : 125\\
    }

    """

    result = get_film(id)
    return {"status_code": 200 , "filme" : result}

@router.post("/filmes/", summary="Cadastra um novo filme")
async def cadastra_filmes(film: Filme):

    """
    Cria um filme com as seguintes informações

    - **name**: Título do filme
    - **description** : breve sinopse do filme
    - **release_year** : ano de lançamento do filme
    - **length** : duração do filme em minutos
    
    """

    result = create_film(film)

    if(result == "OK"):
        return {"status_code": 201 }  
    else:
        return {"status_code": 404 , "mensagem":result }  

@router.put("/filmes/{id}/" , summary="Atualiza a informação de um filme")
async def update_filme(id: int , film: Filme):

    """
    Atualiza o filme de {id} correspondente, com possibilidade de mudança nos seguintes campos:

    - **name**: Título do filme
    - **description** : breve sinopse do filme
    - **release_year** : ano de lançamento do filme
    - **length** : duração do filme em minutos
    
    """

    result = update_film(id , film.dict())

    if(result == "OK"):
        return {"status_code": 200 } 
    else:
        return {"status_code": 404 , "mensagem":result }

@router.delete("/filmes/{id}", summary="Deleta o filme do {id} especificado")
async def deleta_filme(id: int): 
    result = delete_film(id)
    return {"status_code": 200 } 