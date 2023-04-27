# Neste arquivo teremos funções reutilizáveis para interagir com os dados do banco de dados.

#  ------------> Read data <------------

from sqlalchemy.orm import Session

from .models import User , Item
from .schemas import *

def get_user(db: Session, user_id: int):
    '''
    Retorna usuário do id pedido.
    '''
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    '''
    Retorna usuário do email pedido.
    '''
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    '''
    Retorna todos os usuários.
    '''
    return db.query(models.User).offset(skip).limit(limit).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    '''
    Retorna todo os items do banco.
    '''
    return db.query(models.Item).offset(skip).limit(limit).all()

#  ------------> Write data <------------

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user) # Adiciona a nov ainstancia no banco de dados.
    db.commit()     # Salva no banco
    db.refresh(db_user)  # Atualizar sua instancia para  que contenha novos dados do banco de dados, como o ID gerado
    return db_user


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item