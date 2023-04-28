'''
Esse arquivo realiza a comunicação com o banco de dados
'''

from sqlalchemy.orm import Session

from ..models.tables import Movies
from ..schemas.films import *


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    '''
    Retorna todos os filmes.
    '''
    return db.query(Movies).offset(skip).limit(limit).all()


def get_movie_by_tile(db : Session , title : str):
    '''
    Retorna os filmes com o titulo especificado
    '''
    return db.query(Movies).filter(Movies.name == title).all()

def get_movie_by_id(db : Session , id : id):
    '''
    Retorna os filmes com o id especificado
    '''
    return db.query(Movies).filter(Movies.movie_id == id).first()

def register_movie(db : Session , movie : MovieCreate):
    '''
    Cadastra um novo filme
    '''
    new_movie = Movies(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie

def movie_update(db : Session , movie : MovieUpdate , id : int):
    '''
    Atualiza um filme já existente na base de dados
    '''

    # Verifica se o id que se quer atualizar existe: 
    movie_to_update = db.query(Movies).filter(Movies.movie_id == id).first()
    if movie_to_update is None : 
        return None

    db.query(Movies).filter(Movies.movie_id == id).update({'name': movie.name , 'tipo': movie.tipo , 'description': movie.description , 'release_year' : movie.release_year , 'director' : movie.director , 'length' : movie.length })
    db.commit()

    return db.query(Movies).filter(Movies.movie_id == id).first() 


def movie_delete(db : Session , id : int):
    '''
    Deleta um filme caso ele exista na base de dados
    '''

    # Verifica se o id que se quer deletar existe: 
    movie_to_delete= db.query(Movies).filter(Movies.movie_id == id).first()
    if movie_to_delete is None : 
        return None

    db.query(Movies).filter(Movies.movie_id == id).delete()
    db.commit()
    return {'message' : 'O filme foi deletado com sucesso!'}