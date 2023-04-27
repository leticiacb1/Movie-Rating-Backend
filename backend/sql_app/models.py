from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# --------------------------- MODELOS SQLAlchemy ---------------------------

# Relacionamento:
# Conterá os valores de outras tabelas relacionadas a esta.

class User(Base):
    __tablename__ = "users"  # Nome da tabela


    # Atributos representam uma coluna na tabela do database
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Ao acessar os itens de atributos em um User, como em my_user.items, 
    # ele terá uma lista de modelos Item SQLAlchemy (da tabela items) que possuem uma chave estrangeira 
    # apontando para este registro na tabela users
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")