from pydantic import BaseModel


# ----- Ratings -----
class RatingBase(BaseModel):
    comment : str
    score : int


class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    rating_id: int

    class Config:
        orm_mode = True


# ----- Movies -----
class MovieBase(BaseModel):
    name : str
    description : str
    release_year : str
    length : int

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    movie_id: int
    ratings : list[Rating]

    class Config:
        orm_mode = True