from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# app = FastAPI()
router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_user = crud.get_movie_by_name(db, name=movie.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Movie already registered")
    return crud.create_movie(db=db, movie=movie)


@router.get("/movies/", response_model=list[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies


@router.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_movie(db, movie_id=movie_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_user


@router.post("/movies/{movie_id}/ratings/", response_model=schemas.Rating)
def create_rating_for_movie(
    movie_id: int, rating: schemas.RatingCreate, db: Session = Depends(get_db)
):
    return crud.create_movie_rating(db=db, rating=rating, movie_id=movie_id)


@router.get("/ratings/", response_model=list[schemas.Rating])
def read_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ratings = crud.get_ratings(db, skip=skip, limit=limit)
    return ratings