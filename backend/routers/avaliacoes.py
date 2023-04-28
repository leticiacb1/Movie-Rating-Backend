# from fastapi import APIRouter
# from backend.models.base_models import Avaliacao, AvaliacaoUpdate
# from fastapi import status
# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session
# from typing import List

# from . import crud
# from . import models
# from . import schemas

# from .database import SessionLocal, engine

# from ..services.utils_avaliacoes import get_all_rating , create_rating, delete_rating, get_rating, update_rating

# models.Base.metadata.create_all(bind=engine) 
# router = APIRouter()

# # --------- Dependency ---------
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)     # Modelo de retorno é SQLAlchemy                                       


# @router.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)     
#     return users
# Acessar um banco de dados pode levar tempo. Como  SQLAlchemy não possui compatibilidade direta com "awaut" utilizamos o ".first()"

# @router.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
