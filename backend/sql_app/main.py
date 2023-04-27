from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud
from . import models
from . import schemas

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # create the database tables

app = FastAPI()

# Dependency
# Precisamos ter uma sessão/conexão de banco de dados independente por solicitação, 
# usar a mesma sessão em todas as solicitações e fechá-la após a conclusão da solicitação.

# Nossa dependência irá criar um novo SQLAlchemy SessionLocal que será usado em uma única 
# requisição, e então fechá-la assim que a requisição for finalizada.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# O bloco "try/except" garante que a sessão do banco de dados seja sempre fechada após a solicitação. 
# Mesmo se houver uma exceção durante o processamento da solicitação.

    
# ------------ FAST API OPERATION CODE  ------------
# Estamos criando a sessão do banco de dados antes de cada solicitação na dependência com yield e fechando-a depois.
# E então podemos criar a dependência necessária na função de operação de caminho, para obter essa sessão diretamente.
# Com isso, podemos apenas chamar crud.get_user diretamente de dentro da função de operação de caminho e usar essa sessão.

# -------------- MIGRATIONS --------------
# Como estamos usando o SQLAlchemy diretamente e não precisamos de nenhum tipo de plug-in para funcionar com o FastAPI

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)     # Modelo de retorno é SQLAlchemy                                       


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)     
    return users
# Acessar um banco de dados pode levar tempo. Como  SQLAlchemy não possui compatibilidade direta com "awaut" utilizamos o ".first()"

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items