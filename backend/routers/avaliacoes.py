from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..schemas.rating import *
from ..services.crud_avaliacoes import *

from ..sql_app.database import Base , engine , SessionLocal

Base.metadata.create_all(bind=engine) 
router = APIRouter()

# --------- Dependency ---------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/ratings/", response_model=List[Rating] , summary="Retorna todas as avaliações da base de dados")
def read_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''
    Retorna as informações de todos as avaliações da base no formato:
    
    [\\
        {\\
            **"comment"**: "Ótimo filme , chorei muito",\\
            **"score"**: 5,\\
            **"movie_id"**: 1,\\
            **"rating_id"**: 1\\
        },\\
        ...\\
    ]

    Caso a base não possua avaliações , o resultado será uma "vazio".
    O significado de cada campo retornado pode ser encontrado a seguir:

    - **comment**: Comentario para o filme.
    - **score**: Nota do usuario, valor entre 0 e 5.
    - **movie_id** : Id do filme a qual a avaliação se refere.
    - **rating_id** : Identificador da avaliação. Dada automaticamente pelo banco.
    '''
    ratings = get_ratings(db, skip=skip, limit=limit)     
    return ratings

@router.get("/ratings/{movie_id}", response_model=List[Rating] , summary="Retorna todas as avaliações cadastradas para o filme especificado")
def read_rating_by_movie_title(movie_id: int , db: Session = Depends(get_db)):
    '''
    Retorna as informações de todas as avaliações da base que possuem relação com o filme indicado:
    
    [\\
        {\\
            **"comment"**: "Ótimo filme , chorei muito",\\
            **"score"**: 5,\\
            **"movie_id"**: 1,\\
            **"rating_id"**: 1\\
        },\\
        ...\\
    ]
    
    '''
    ratings = get_rating_by_movie_id(db, id = movie_id)
    if ratings is None:
        raise HTTPException(status_code=404, detail="[ERROR] Filme não cadastrado.")
    return ratings

@router.post("/ratings/", response_model= Rating , summary="Cadastra uma avaliação")
def create_rating(rating : RatingCreate, db: Session = Depends(get_db)):
    
    '''
    Para o cadastro de uma nova avaliação , as seguintes informações precisam ser especificadas

    - **comment**: Comentario para o filme. Formato em string.
    - **score**: Nota do usuario, valor entre 0 e 5. Formato inteiro.
    - **movie_id** : Id do filme a qual a avaliação se refere. Formato em string.
    - **rating_id** : Identificador da avaliação. Dada automaticamente pelo banco. Formato inteiro.
    
    '''
    new_rating = register_rating(db=db, rating=rating)

    if new_rating is None:
       raise HTTPException(status_code=404, detail=f" [ERROR] Não existe filme com id={rating.movie_id} cadastrado.")
    return new_rating 

@router.put("/ratings/{id}", response_model= Rating , summary="Atualiza a avaliação com o id especificado")
def update_rating(rating : RatingUpdate, db: Session = Depends(get_db) , id = id):
    '''
    Atualiza a avaliação de {id} correspondente, com possibilidade de mudança nos seguintes campos:
    
    - **comment**: Comentario para o filme. Formato em string.
    - **score**: Nota do usuario, valor entre 0 e 5. Formato inteiro.
    
    Para realizar a atualização de um filme:
    
    1 - Preencher o campo id com o valor correspondente da avaliação que se quer modificar.\\

    2 - Preencher o dicionário com as mudanças, toda informação será reescrita. 

    {\\
        **"comment"**: "string",\\
        **"score"**: 0\\
    }
    '''
    rating = rating_update(db=db, rating=rating , id = id) 
    if rating is None:
        raise HTTPException(status_code=404, detail=" [ERROR] Avaliação não encontrada.")
    return rating

@router.delete("/ratings/{id}" , summary="Deleta a avaliacao com o id especificado")
def delete_rating(db: Session = Depends(get_db) , id = id):
    '''
        Deletar a avaliação que possui o {id} fornecido.\\
        Para apagar uma avaliação, basta indicar o {id} (Inteiro) da avaliação que se deseja apagar.
    '''
    rating = rating_delete(db=db, id = id) 
    if rating is None:
        raise HTTPException(status_code=400, detail=" [ERROR]  Avaliação não existe para ser apagada da base.")
    return rating
