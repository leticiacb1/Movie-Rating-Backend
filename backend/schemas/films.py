from pydantic import BaseModel , Field
from  typing  import  List
from .rating import Rating

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
    ratings: List [ Rating ]
    
    class  Config :
        orm_mode  =  True