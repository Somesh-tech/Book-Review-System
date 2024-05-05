from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from db_conn.db_config import engine, Sessionlocal, get_db
from db_conn import models
from db_conn import schemas
import json


router = APIRouter(prefix="/all_books", tags= ["BOOKS"])

list_of_books = []


@router.get("/")
def all_books(db: Session = Depends(get_db)):

    retrieve_books = db.query(models.Book).all()
    list_of_books = []

    for book in retrieve_books:
        book_data = {
            "title": book.title,
            "author": book.author,
            "pub_year": book.pub_year,
        }
        list_of_books.append(book_data)
    return {"Result": f"{list_of_books}"}


"""
This endpoint will retrieve all the books with author name as filter.
"""


@router.get("/{author}")
def all_books(author: str, db: Session = Depends(get_db)):
    list_of_books.clear()
    retrieve_books = db.query(models.Book).where(models.Book.author == author).all()
    for book in retrieve_books:
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


@router.get("/year/{pub_year}")
def all_books(pub_year: int, db: Session = Depends(get_db)):
    list_of_books.clear()
    retrieve_books = db.query(models.Book).where(models.Book.pub_year == pub_year).all()
    for book in retrieve_books:
        book_data = {
            "title": book.title,
            "author": book.author,
            "pub_year": book.pub_year,
        }
        list_of_books.append(book_data)
    return {"Result": f"{list_of_books}"}


@router.post("/add_book")
def add_book(book_details: schemas.Book_Details, db: Session = Depends(get_db)):
    new_book = models.Book(**book_details.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@router.delete("/delete/{title}")
def delete_book(title: str, db: Session = Depends(get_db)):
    delete_book = db.query(models.Book).filter(models.Book.title == title)
    if delete_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{title} is not Found."
        )
    delete_book.delete(synchronize_session=False)
    db.commit()
    return f"{title} has been removed from database."


@router.put("/update/{title}")
def update_book(title: str, book: schemas.Book_Details, db: Session = Depends(get_db)):
    update = db.query(models.Book).where(models.Book.title == title)

    if not update.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{title} is not Found."
        )
    update.update(book.dict(), synchronize_session=False)
    db.commit()

    return f"{title} has been updated."
