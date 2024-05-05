from typing import Optional
from pydantic import BaseModel, EmailStr

"""
This class will handle the data validation for Book's.
"""


class Book_Details(BaseModel):
    title: str
    author: str
    pub_year: int


class Response(BaseModel):
    class Config:
        orm_mode = True


"""
This class will handle the data validation for Review's.
"""


class Review_details(BaseModel):
    desc: str
    rating: int
    title: str
    pub_year: int


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenData(BaseModel):
    id: Optional[str] = str


class Categories(BaseModel):
    genre: str
    age: int
