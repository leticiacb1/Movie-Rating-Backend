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

    filmes : {

    **filme_id** : {\\
            name : "Titanic",\\
            description : " Um filme que mistura um jovem romance com uma infeliz tragédia.",\\
            release_year 1998,\\
            length : 125\\
    },

    ...

    }

    Caso a base não possua filmes , o resultado será "vazio".\\
    Em caso de erro, uma exceção será levantava indicando o motivo do erro.

    """

    result = get_all_films()
    return {"status_code": 200 , "filmes" : result}

@router.get("/filmes/{id}" , summary="Retorna filme do id especificado")
async def get_filme_id(id: int):

    """
    Retorna as informação do filme com o respectivo {id}, no formato:

   filme : {

    **filme_id** : {\\
            name : "Titanic",\\
            description : " Um filme que mistura um jovem romance com uma infeliz tragédia.",\\
            release_year 1998,\\
            length : 125\\
    }\\
    }

    Caso o filme não exista na base, o resultado será "vazio".

    """

    result = get_film(id)
    return {"status_code": 200 , "filme" : result}

@router.post("/filmes/", summary="Cadastra um novo filme")
async def cadastra_filmes(film: Filme):

    """
    Cria um filme com as seguintes informações

    - **name**: Título do filme . Campo do tipo string.
    - **description** : breve sinopse do filme. Campo do tipo string.
    - **release_year** : ano de lançamento do filme. Campo do tipo inteiro.
    - **length** : duração do filme em minutos.Campo do tipo inteiro.
    
    Para criar um filme, deve ser preenchido os campos a seguir:

    {\\
    **"name"**: "Titanic",\\
    **"description"**: "Um filme que mistura um jovem romance com uma infeliz tragédia.",\\
    **"release_year"**: 1998,\\
    **"length"**: 125\\
    }
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

    - **name**: Título do filme . Campo do tipo string.
    - **description** : breve sinopse do filme. Campo do tipo string.
    - **release_year** : ano de lançamento do filme. Campo do tipo inteiro.
    - **length** : duração do filme em minutos.Campo do tipo inteiro.
    
    Para realizar a atualização de um filme:

    1 - Preencher o campo id com o valor correspondente do filme que se quer modificar.\\

    2 - Preencher o dicionário com as mudanças, toda informação será reescrita. 

    {\\
    **"name"**: "Titanic",\\
    **"description"**: "Um filme que mistura um jovem romance com uma infeliz tragédia.",\\
    **"release_year"**: 1998,\\
    **"length"**: 125\\
    }
    
    """

    result = update_film(id , film.dict())

    if(result == "OK"):
        return {"status_code": 200 } 
    else:
        return {"status_code": 404 , "mensagem":result }

@router.delete("/filmes/{id}", summary="Deleta o filme do {id} especificado")
async def deleta_filme(id: int): 

    """
    Deleta o filme que possui o {id} fornecido.

    Para apagar um filme, basta indicar o {id} (Inteiro) do filme que se deseja apagar.
    """

    result = delete_film(id)
    return {"status_code": 200 } 