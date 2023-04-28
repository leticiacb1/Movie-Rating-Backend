from pydantic import BaseModel , Field
from  typing  import  List

class RatingBase(BaseModel):
    comment : str
    score : int = Field(default = 1 , gt=0, le=5)

class RatingCreate(RatingBase):
    movie_id : int 
    pass

class RatingUpdate(RatingBase):
    pass

class Rating(RatingBase):
    movie_id : int 
    rating_id: int

    class Config:
        orm_mode = True