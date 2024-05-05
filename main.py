"""
This doc will contain all the endpoints required.
"""

from db_conn.db_config import engine, Sessionlocal, get_db
import db_conn.models as models
from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import json
from routes import book, reviews, users
from routes import login

"""
Initiating FastApi and connection to the database.
"""
app = FastAPI(title="Book Review System")


models.Base.metadata.create_all(bind=engine)

app.include_router(book.router)
app.include_router(reviews.router)
app.include_router(users.router)
app.include_router(login.router)
