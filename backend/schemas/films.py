from pydantic import BaseModel , Field
from  typing  import  List

class MovieBase(BaseModel):
    name : str
    tipo : str
    description : str = Field(default = None, description="Resumo do filme")
    release_year : int 
    director : str
    length: int

class MovieCreate(MovieBase):
    pass

class MovieUpdate(MovieBase):
    pass

class Movie (MovieBase):
    movie_id: int
    ratings: List [ Avaliacao ]
    
    class  Config :
        orm_mode  =  True