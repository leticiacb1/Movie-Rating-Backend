from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..sql_app.database import Base

# --------------------------- MODELOS SQLAlchemy ---------------------------

# Relacionamento:
# Conterá os valores de outras tabelas relacionadas a esta.

class Movies(Base):
    __tablename__ = "movies"  

    movie_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True)
    tipo = Column(String, index=True)
    description = Column(String, unique=True, index=True)
    release_year = Column(Integer, index=True)
    director = Column(String, index=True)
    length = Column(Integer, default=True)

    ratings = relationship("Ratings", back_populates="films")


class Ratings(Base):
    __tablename__ = "ratings"

    rating_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    score = Column(Integer, index=True)
    comment = Column(String, index=True)
    movie_id = Column(Integer, ForeignKey("movies.movie_id"))

    films = relationship("Movies", back_populates="ratings")