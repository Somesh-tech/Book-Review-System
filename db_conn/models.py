from pydantic import EmailStr
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db_conn.db_config import Base
from uuid import uuid4

class Book(Base):
    __tablename__ = "Book"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,default=uuid4)
    title = Column(String, name="Title", unique=True,index=True)
    author = Column(String, name="Author")
    pub_year = Column(Integer, name="Year_of_Publication")

    
class Review(Base):
    __tablename__ = "Review"

    id = Column(UUID(as_uuid=True), nullable=False, default=uuid4,primary_key=True)
    desc = Column(String,index=True)
    rating = Column(Integer, index=True)
    title = Column(String, index=True)
    pub_year = Column(Integer, index=True)
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'),index=True)

class Users(Base):
        __tablename__ = "users"
        
        id = Column(UUID(as_uuid=True), nullable=False, default=uuid4,primary_key=True)
        email = Column(String, index=True, unique=True)
        name = Column(String, index=True)
        password = Column(String, nullable=False)
        created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'),index=True)
