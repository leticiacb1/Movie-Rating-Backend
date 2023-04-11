from pydantic import BaseModel , Field
from fastapi import Query
from enum import Enum

from datetime import datetime

class Avaliacao(BaseModel):
    id: int
    film_id : int 
    comment : str = Field(default = None, description="Descricao da avaliação")
    score : int = Field(default = 1 , gt=0, le=5)

class Filme(BaseModel):
    film_id : int
    name : str
    description : str = Field(default = None, description="Resumo do filme")
    release_year : int 
    length: int