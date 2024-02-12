from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from db_conn.db_config import Base
from uuid import uuid4

class Book(Base):
    __tablename__ = "Book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, name="Title", unique=True,index=True)
    author = Column(String, name="Author")
    pub_year = Column(Integer, name="Year_of_Publication")

    
class Review(Base):
    __tablename__ = "Review"

    # id = Column(UUID(as_uuid=True), , default=uuid4)
    desc = Column(String, primary_key=True,index=True)
    rating = Column(Integer, index=True)
    title = Column(String, index=True)
    pub_year = Column(Integer, index=True)
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'),index=True)
    