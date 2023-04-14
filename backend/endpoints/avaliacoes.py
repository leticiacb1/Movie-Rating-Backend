from fastapi import APIRouter
from backend.models.base_models import Avaliacao, AvaliacaoUpdate
from fastapi import status
import json

from ..services.utils_avaliacoes import get_all_rating , create_rating, delete_rating, get_rating, update_rating

router = APIRouter()

@router.get("/avaliacoes/", summary="Retorna todas as avaliações da base de dados")
async def get_all_avaliacoes():

    """
    Retorna as informações de todas as avaliações da base no formato:

    avaliacoes : {

    **rating_id** : {\\
            film_id : 1,\\
            comment : "Gostei muito do filme!",\\
            score: 5\\
    },

    ...

    }

    Caso a base não possua avaliações , o resultado será "vazio".\\
    Em caso de erro, uma exceção será levantava indicando o motivo do erro.

    """
    result = get_all_rating()
    return {"status_code": 200 , "avaliacoes" : result}

@router.get("/avaliacoes/{id}", summary="Retorna avaliações do filme de id especificado")
async def get_avaliacao_id(id: int):

    """
    Retorna as avaliações do filme de id especificado, no formato:

   avaliacao : {

    **rating_id** : {\\
            film_id : 1,\\
            comment : "Gostei muito do filme!",\\
            score: 5\\
    },
    ...
    }

    Caso não exista avaliação para esse filme, resultado será "vazio".

    """
    result, list_ratings = get_rating(id)
    return {"status_code": 200 , "mensagem" : result, "avaliações" : list_ratings}

@router.post("/avaliacoes/", summary="Cadastra uma nova avaliação")
async def cadastra_avaliacao(rate: Avaliacao):

    """
    Cria uma avaliação com as seguintes informações

    - **film_id**: id do filme relacionado a avaliação. Campo do tipo int.
    - **comment** : comentário sobre o filme. Campo do tipo string.
    - **score** : nota (entre 0-5) para o filme. Campo do tipo inteiro.
    
    Para criar um filme, deve ser preenchido os campos a seguir:

    {\\
    **film_id**: 1,\\
    **comment**: "Gostei muito do filme!",\\
    **score**: 5\\
    }
    """

    result = create_rating(rate)

    if(result == "OK"):
        return {"status_code": 201 , "mensagem": result}  
    else:
        return {"status_code": 404 , "mensagem":result }  

@router.put("/avaliacoes/{id}/", summary="Atualiza a informação de uma avaliação")
async def update_avaliacao(id: int , film: AvaliacaoUpdate):

    """
    Atualiza a avaliação de {id} correspondente, com possibilidade de mudança nos seguintes campos:

    - **comment** : comentário sobre o filme. Campo do tipo string.
    - **score**   : nota (entre 0-5) para o filme. Campo do tipo inteiro. 
    
    Para realizar a atualização de uma avaliação:

    1 - Preencher o campo id com o valor correspondente da avaliação que se quer modificar.\\

    2 - Preencher o dicionário com as mudanças, toda informação será reescrita. 

    {\\
    **comment**: "Gostei muito do filme!",\\
    **score**: 5\\
    }
    
    """

    result = update_rating(id , film.dict())

    if(result == "OK"):
        return {"status_code": 200 } 
    else:
        return {"status_code": 404 , "mensagem":result }


@router.delete("/avaliacoes/{id}", summary="Deleta o filme do id especificado")
async def deleta_avaliacao(id: int):

    """
    Deleta a avaliação que possui o {id} fornecido.

    Para apagar uma avaliação, basta indicar o {id} (Inteiro) da avaliação que se deseja apagar.
    """

    result = delete_rating(id)
    return {"status_code": 200 } 