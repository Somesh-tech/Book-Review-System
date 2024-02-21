from db_conn.schemas import UserLogin
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db_conn.db_config import get_db
from fastapi import APIRouter
from utils import utils
from db_conn import models
from authentication import OAuth
router = APIRouter()

@router.post('/login')
def login(login_creds:UserLogin, db: Session = Depends(get_db)):
    
    user = db.query(models.Users).filter(models.Users.email == login_creds.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid User")
    
    if not utils.verify_pwd(login_creds.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid User")
    
    token = OAuth.generate_token(data={"user": login_creds.email})

    return {"Token" : f"{token}", "Token_type": "bearer"}
