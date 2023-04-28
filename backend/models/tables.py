from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# --------------------------- MODELOS SQLAlchemy ---------------------------

# Relacionamento:
# Conterá os valores de outras tabelas relacionadas a esta.

class Movies(Base):
    __tablename__ = "movies"  

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True)
    tipo = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)
    release_year = Column(Integer, index=True)
    director = Column(String, index=True)
    length = Column(Integer, default=True)

    ratings = relationship("Rating", back_populates="films")


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    score = Column(Integer, index=True)
    comment = Column(String, index=True)
    film_id = Column(Integer, ForeignKey("movies.id"))

    films = relationship("Movies", back_populates="ratings")