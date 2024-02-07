"""
This doc will contain all the endpoints required.
"""
from db_config import engine, Sessionlocal
import models
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

"""
Initiating FastApi and connection to the database.
"""
app = FastAPI()
db =  Sessionlocal()
models.Base.metadata.create_all(bind=engine) 

"""
This class will handle the data validation for Book's.
"""
class Book_Details(BaseModel):
    title: str
    author: str
    pub_year: int

"""
This class will handle the data validation for Review's.
"""
class Review_details(BaseModel):    
    desc: str
    rating: int
    title: str
    pub_year: int


"""
Initiating a lst to loop over the object attributes that will be fetched from the ORM.
"""
l1=[]

"""
This endpoint will retrieve all the books with no filter.
"""
@app.get("/all_books")
def all_books():
    
    retrieve_books = db.query(models.Book).all()
    for book in retrieve_books:  # Assuming books_list is the list of Book objects
        book_data = {
        "title": book.title,
        "author": book.author,
        "pub_year": book.pub_year
        }
        l1.append(book_data) 
    return {"Result" : f"{l1}"}

"""
This endpoint will retrieve all the books with author name as filter.
"""
@app.get("/all_books/{author}")
def all_books(author: str):
    l1.clear()
    retrieve_books = db.query(models.Book).where(models.Book.author == author).all()
    for book in retrieve_books:  # Assuming books_list is the list of Book objects
        book_data = {
        "title": book.title,
        "author": book.author,
        "pub_year": book.pub_year
        }
        l1.append(book_data) 
    return {"Result" : f"{l1}"}

"""
This endpoint will retrieve all the books with publication year as filter.
"""
@app.get("/all_books/year/{pub_year}")
def all_books(pub_year : int):
    l1.clear()
    retrieve_books = db.query(models.Book).where(models.Book.pub_year == pub_year).all()
    for book in retrieve_books:  # Assuming books_list is the list of Book objects
        book_data = {
        "title": book.title,
        "author": book.author,
        "pub_year": book.pub_year
        }
        l1.append(book_data) 
    return {"Result" : f"{l1}"}

"""
This endpoint will retrieve all the reviews for a specific book.
"""
@app.get("/view_review/{title}")
def book_reviews(title : str):
    l1.clear()
    review = db.query(models.Review).where(models.Review.title == title).all()
    for book in review:  
        book_data = {
        "title": book.title,
        "pub_year": book.pub_year,
        "desc" : book.desc,
        "rating" : book.rating
        }
        l1.append(book_data) 
    return {"Result" : f"{l1}"}

"""
This endpoint will create a new record for submiting a book review.
"""
@app.post("/submit_review")
def submit_review(review: Review_details):
    new_review = models.Review(desc="",rating="",title="",pub_year="")
    db.add(new_review)
    db.commit()

    return {"Result" :"New Review has been submitted" }

"""
This endpoint will create a new record for every new book.
"""
@app.post("/add_book")
def add_book(book_details: Book_Details):
    new_book = models.Book(title=book_details.title, author=book_details.author, pub_year=book_details.pub_year)
    db.add(new_book)
    db.commit()

    return {"Result" : "New book added."}


