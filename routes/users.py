from fastapi import APIRouter, Depends, HTTPException,status
from db_conn.schemas import UserCreate
from sqlalchemy.orm import Session
from db_conn.db_config import get_db
from db_conn import models
from db_conn import schemas
from passlib.context import CryptContext
from utils import utils

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/users/{name}")
def get_user(name: str, db:Session=Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.name == name).first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user

@router.post("/add_user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # we will take the user password from "user"variable and 
    # then hash the pwd and then reassign it

    # hash_pwd = pwd_context.hash(user.password)
    hash_pwd = utils.hash_pwd(user.password)
    user.password = hash_pwd

    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
