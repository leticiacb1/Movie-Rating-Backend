from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Movies(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    release_year = Column(Integer)
    length = Column(Integer)

    ratings = relationship("Ratings", back_populates="owner")


class Ratings(Base):
    __tablename__ = "ratings"

    rating_id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.movie_id"))
    comment = Column(String)
    score = Column(Integer)

    owner = relationship("Movies", back_populates="ratings")