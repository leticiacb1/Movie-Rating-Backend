from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..schemas.films import *
from ..services.crud_filmes import *

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

@router.get("/movies/", response_model=List[Movie] , summary="Retorna todos os filmes da base de dados")
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''
    Retorna as informações de todos os filmes da base no formato:
    
    {\\
        {\\
            **"name"**: "string",\\
            **"tipo"**: "string",\\
            **"description"**: "string",\\
            **"release_year"**: 0,\\
            **"director"**: "string",\\
            **"length"**: 0,\\
            **"movie_id"**: 0,\\
            **"ratings"**: [ ... ]\\
        }\\
    ...\\
    }

    Caso a base não possua filmes , o resultado será uma "vazio".
    O significado de cada campo retornado pode ser encontrado a seguir:

    - **name**: Título do filme .
    - **tipo**: Tipo do filmes [Ex : Drama , Romance etc].
    - **description** : breve sinopse do filme. 
    - **release_year** : ano de lançamento do filme. 
    - **director** : diretor do filme.
    - **length** : duração do filme em minutos.
    - **movie_id** : identifiação atribuida automaticamente pelo banco de dados.
    - **rating** : lista com as avaliações dada para esse filme.

    '''

    movies = get_movies(db, skip=skip, limit=limit)     
    return movies

@router.get("/movies/{title}", response_model=List[Movie] , summary="Retorna todos os filmes cadastrados com o nome especificado")
def read_movie_by_title(title: str , db: Session = Depends(get_db)):
    '''
    Retorna as informações de todos os filmes da base que possuem o nome especificado:
    
    {\\
        {\\
            **"name"**: "string",\\
            **"tipo"**: "string",\\
            **"description"**: "string",\\
            **"release_year"**: 0,\\
            **"director"**: "string",\\
            **"length"**: 0,\\
            **"movie_id"**: 0,\\
            **"ratings"**: [ ... ]\\
        }\\
    ..\\
    }

    Caso a base não possua filmes , o resultado será "vazio".
    
    '''

    movie = get_movie_by_tile(db, title = title)
    if movie is None:
        raise HTTPException(status_code=404, detail=" [ERROR] Filme não encontrado")
    return movie

@router.post("/movies/", response_model= Movie , summary="Cadastra um nome filme")
def create_movie(movie : MovieCreate, db: Session = Depends(get_db)):

    '''
    Para o cadastro de um novo filme , as seguintes informações precisam ser especificadas

    - **name**: Título do filme . Formato string.
    - **tipo**: Tipo do filmes [Ex : Drama , Romance etc]. Formato string.
    - **description** : breve sinopse do filme. Formato string.
    - **release_year** : ano de lançamento do filme. Formato inteiro.
    - **director** : diretor do filme. Formato string.
    - **length** : duração do filme em minutos. Formato inteiro.
    
    '''

    return register_movie(db=db, movie=movie)     

@router.put("/movies/{id}", response_model= Movie , summary="Atualiza o filme com o id especificado")
def update_movie(movie : MovieUpdate, db: Session = Depends(get_db) , id = id):
    '''
    Atualiza o filme de {id} correspondente, com possibilidade de mudança nos seguintes campos:
    
    - **name**: Título do filme . Formato string.
    - **tipo**: Tipo do filmes [Ex : Drama , Romance etc]. Formato string.
    - **description** : breve sinopse do filme. Formato string.
    - **release_year** : ano de lançamento do filme. Formato inteiro.
    - **director** : diretor do filme. Formato string.
    - **length** : duração do filme em minutos. Formato inteiro.
    
    Para realizar a atualização de um filme:
    
    1 - Preencher o campo id com o valor correspondente do filme que se quer modificar.\\

    2 - Preencher o dicionário com as mudanças, toda informação será reescrita. 

    {\\
        **"name"**: "string",\\
        **"tipo"**: "string",\\
        **"description"**: "string",\\
        **"release_year"**: 0,\\
        **"director"**: "string",\\
        **"length"**: 0\\
    }
    '''

    movie = movie_update(db=db, movie=movie , id = id) 
    if movie is None:
        raise HTTPException(status_code=404, detail=" [ERROR] Filme não encontrado para ser atualizado.")
    return movie

@router.delete("/movies/{id}" , summary="Deleta o filme com o id especificado")
def delete_movie(db: Session = Depends(get_db) , id = id):
    '''
        Deleta o filme que possui o {id} fornecido.\\
        Para apagar um filme, basta indicar o {id} (Inteiro) do filme que se deseja apagar.
    '''

    movie = movie_delete(db=db, id = id) 
    if movie is None:
        raise HTTPException(status_code=400, detail=" [ERROR]  Filme não existe para ser apagado da base.")
    return movie