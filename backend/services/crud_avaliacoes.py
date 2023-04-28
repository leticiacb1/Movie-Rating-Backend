'''
Esse arquivo realiza a comunicação com o banco de dados
'''

from sqlalchemy.orm import Session

from ..models.tables import Ratings , Movies
from ..schemas.rating import *

def get_ratings(db : Session, skip : int = 0 , limit : int = 100):
    '''
    Retorna todos as avaliações.
    '''
    return db.query(Ratings).offset(skip).limit(limit).all()

def get_rating_by_movie_id(db : Session , id : int):
    '''
    Retorna as avaliacoes dos filmes com o titulo especificado
    '''

    # Verifica se existe o filme na base de dados:
    movie = db.query(Movies).filter(Movies.movie_id == id).first()
    if(movie == None):
        return None

    return db.query(Ratings).filter(Ratings.movie_id == id).all()

def register_rating(db : Session , rating : RatingCreate):
    '''
    Cadastra uma nova avaliação
    '''

    # Verifica se existe o filme na base de dados:
    movie = db.query(Movies).filter(Movies.movie_id == rating.movie_id).first()

    if(movie == None):
        return None

    new_rating = Ratings(**rating.dict())
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)

    return new_rating  


def rating_update(db : Session , rating : RatingUpdate , id : int):
    '''
    Atualiza uma avaliação já existente na base de dados
    '''

    # Verifica se o id que se quer atualizar existe: 
    rating_to_update = db.query(Ratings).filter(Ratings.rating_id == id).first()
    if rating_to_update is None : 
        return None

    db.query(Ratings).filter(Ratings.rating_id == id).update({'score' : rating.score , 'comment' : rating.comment})
    db.commit()

    return db.query(Ratings).filter(Ratings.rating_id == id).first() 

def rating_delete(db : Session , id : int):
    '''
    Deleta uma avaliação caso ela exista na base de dados
    '''

    # Verifica se o id que se quer deletar existe: 
    rating_to_delete = db.query(Ratings).filter(Ratings.rating_id == id).first()
    if rating_to_delete is None : 
        return None

    db.query(Ratings).filter(Ratings.rating_id == id).delete()
    db.commit()
    return {'message' : 'A avaliação foi deletada com sucesso!'}
