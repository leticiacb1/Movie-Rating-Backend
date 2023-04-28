from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..schemas.films import *
from ..services.utils_filmes import *

from ..sql_app.database import *

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

@router.get("/films/", response_model=List[Movie])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = get_movies(db, skip=skip, limit=limit)     
    return movies
# Acessar um banco de dados pode levar tempo. Como  SQLAlchemy não possui compatibilidade direta com "awaut" utilizamos o ".first()"
