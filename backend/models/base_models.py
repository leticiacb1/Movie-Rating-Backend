from pydantic import BaseModel , Field
from fastapi import Query
from enum import Enum

from datetime import datetime

class Avaliacao(BaseModel):
    avaliacao_id: int
    film_id : int 
    comentario : str = Field(default = None, description="Descricao da avaliação")
    nota : str = Query(default = 1 , choices=(1,2,3,4,5))

class Filme(BaseModel):
    film_id : int
    nome : str
    description : str = Field(default = None, description="Resumo do filme")
    release_year : int 
    length: int