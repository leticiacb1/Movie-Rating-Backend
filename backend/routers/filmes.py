from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..schemas.films import *
from ..services.crud_filmes import *

from ..sql_app.database import Base , engine , SessionLocal

Base.metadata.create_all(bind=engine)
#models.Base.metadata.create_all(bind=engine) 
router = APIRouter()

# --------- Dependency ---------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/movies/", response_model=List[Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = get_movies(db, skip=skip, limit=limit)     
    return movies

@router.get("/movies/{title}", response_model=List[Movie])
def read_movie_by_title(title: str , db: Session = Depends(get_db)):
    movie = get_movie_by_tile(db, title = title)
    if movie is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return [movie]

@router.post("/movies/", response_model= Movie)
def create_movie(movie : MovieCreate, db: Session = Depends(get_db)):
    return create_film(db=db, movie=movie)     

