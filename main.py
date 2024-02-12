"""
This doc will contain all the endpoints required.
"""

from db_conn.db_config import engine, Sessionlocal, get_db
import db_conn.models as models
from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import json
"""
Initiating FastApi and connection to the database.
"""
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

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


"""
Initiating a lst to loop over the object attributes that will be fetched from the ORM.
"""
list_of_books = []
list_of_reviews = []

"""
This endpoint will retrieve all the books with no filter.
"""


@app.get("/all_books")
def all_books(db: Session = Depends(get_db)):

    retrieve_books = db.query(models.Book)
    list_of_books = {}

    for book in retrieve_books:  # Assuming books_list is the list of Book objects
        book_data = {
            "title": book.title,
            "author": book.author,
            "pub_year": book.pub_year,
        }
        list_of_books["Books"] = book_data

    data = json.dumps(list_of_books)
        

    return {"Result": f"{data}"}


"""
This endpoint will retrieve all the books with author name as filter.
"""


@app.get("/all_books/{author}")
def all_books(author: str,db: Session = Depends(get_db)):
    list_of_books.clear()
    retrieve_books = db.query(models.Book).where(models.Book.author == author).all()
    for book in retrieve_books:  # Assuming books_list is the list of Book objects
        book_data = {
            "title": book.title,
            "author": book.author,
            "pub_year": book.pub_year,
        }
        list_of_books.append(book_data)
    return {"Result": f"{list_of_books}"}


"""
This endpoint will retrieve all the books with publication year as filter.
"""


@app.get("/all_books/year/{pub_year}")
def all_books(pub_year: int, db: Session = Depends(get_db)):
    list_of_books.clear()
    retrieve_books = db.query(models.Book).where(models.Book.pub_year == pub_year).all()
    for book in retrieve_books:  # Assuming books_list is the list of Book objects
        book_data = {
            "title": book.title,
            "author": book.author,
            "pub_year": book.pub_year,
        }
        list_of_books.append(book_data)
    return {"Result": f"{list_of_books}"}


"""
This endpoint will retrieve all the reviews for a specific book.
"""


@app.get("/view_review/{title}")
def book_reviews(title: str, db: Session = Depends(get_db)):
    list_of_books.clear()
    review = db.query(models.Review).where(models.Review.title == title).all()
    for book in review:
        book_data = {
            "title": book.title,
            "pub_year": book.pub_year,
            "desc": book.desc,
            "rating": book.rating,
        }
        
        list_of_books.append(book_data)
    return {"Result": f"{list_of_books}"}


"""
This Endpoint will get all the review there is.
"""


@app.get("/all_reviews")
def get_all_reviews(db: Session = Depends(get_db)):

    all_review = db.query(models.Review).all()
    for i in all_review:
        all_review_dict = {
            "desc": i.desc,
            "rating": i.rating,
            "title": i.title,
            "pub_year": i.pub_year,
        }
        list_of_reviews.append(all_review_dict)
    return {"Output": f"{list_of_reviews}"}


"""
This endpoint will create a new record for submiting a book review.
"""


@app.post("/submit_review")
def submit_review(review: Review_details, db: Session = Depends(get_db)):
    new_review = models.Review(
        desc=review.desc,
        rating=review.rating,
        title=review.title,
        pub_year=review.pub_year,
    )
    db.add(new_review)
    db.commit()

    return {"Result": "New Review has been submitted"}


"""
This endpoint will create a new record for every new book.
"""


@app.post("/add_book")
def add_book(book_details: Book_Details, db: Session = Depends(get_db)):
    new_book = models.Book(
        title=book_details.title,
        author=book_details.author,
        pub_year=book_details.pub_year,
    )
    db.add(new_book)
    db.commit()

    return {"Result": "New book added."}

"""The below endpoint will delete the review."""

@app.delete("/delete/{pub_year}")
def delte_post(pub_year : int, db:Session=Depends(get_db)):
    delete_review = db.query(models.Review).filter(models.Review.pub_year == pub_year)
    if delete_review is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Provided book {title} is not Found.")
    delete_review.delete(synchronize_session=False)
    db.commit()
