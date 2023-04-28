from sqlalchemy.orm import Session

from . import models, schemas


# ----- Movies -----
def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.movie_id == movie_id).first()


def get_movie_by_name(db: Session, name: str):
    return db.query(models.Movie).filter(models.Movie.name == name).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(
        name = movie.name,
        description = movie.description,
        release_year = movie.release_year,
        length = movie.length)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# ----- Ratings -----

def get_ratings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rating).offset(skip).limit(limit).all()

def create_movie_rating(db: Session, rating: schemas.RatingCreate, movie_id: int):
    db_rating = models.Rating(**rating.dict(), movie_id=movie_id)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating