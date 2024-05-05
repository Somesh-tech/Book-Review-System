from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from db_conn.db_config import engine, Sessionlocal, get_db
from db_conn import models
from db_conn import schemas
import json

router = APIRouter(prefix="/reviews",tags=["REVIEWS"])

list_of_books = []
list_of_reviews = []

"""
This endpoint will retrieve all the reviews for a specific book.
"""


@router.get("/{title}")
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

        list_of_books.routerend(book_data)
    return {"Result": f"{list_of_books}"}


"""
This Endpoint will get all the review there is.
"""


@router.get("/")
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


@router.post("/new_review")
def submit_review(review: schemas.Review_details, db: Session = Depends(get_db)):
    new_review = models.Review(
        desc=review.desc,
        rating=review.rating,
        title=review.title,
        pub_year=review.pub_year,
    )
    db.add(new_review)
    db.commit()

    return {"Result": "New Review has been submitted"}


"""The below endpoint will delete the review."""


@router.delete("/delete/{pub_year}")
def delete_post(pub_year: int, db: Session = Depends(get_db)):
    delete_review = db.query(models.Review).filter(models.Review.pub_year == pub_year)
    if delete_review is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Provided review {pub_year} is not Found.",
        )
    delete_review.delete(synchronize_session=False)
    db.commit()
    return "Review has been deleted"


"""The below endpoint will update the review."""


@router.put("/update/{title}")
def update_book(
    title: str, review: schemas.Review_details, db: Session = Depends(get_db)
):
    update = db.query(models.Review).where(models.Review.title == title)

    if not update.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{title} is not Found."
        )
    update.update(review.dict(), synchronize_session=False)
    db.commit()

    return f"Review for {title} has been updated."
