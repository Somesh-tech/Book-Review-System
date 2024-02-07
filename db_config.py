from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

Database_Url = "postgresql://postgres:somesh@localhost:5432/book_review_sys"

engine = create_engine(Database_Url)

Base = declarative_base()

Sessionlocal = sessionmaker(bind=engine)