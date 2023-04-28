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

    return db.query(Movies).filter(Movies.name == title).first()

def create_movie(db : Session , movie : MovieCreate):

    new_movie = Movies(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie

def movie_update(db : Session , movie : MovieUpdate , id : int):

   db.query(Movies).filter(Movies.movie_id == id).update({'name': movie.name , 'tipo': movie.tipo , 'description': movie.description , 'release_year' : movie.release_year , 'director' : movie.director , 'length' : movie.length })
   db.commit()
   
   return db.query(Movies).filter(Movies.movie_id == id).first() 

#  ------------> Write data <------------

# def create_user(db: Session, user: UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user) # Adiciona a nov ainstancia no banco de dados.
#     db.commit()     # Salva no banco
#     db.refresh(db_user)  # Atualizar sua instancia para  que contenha novos dados do banco de dados, como o ID gerado
#     return db_user


# def create_user_item(db: Session, item: ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item