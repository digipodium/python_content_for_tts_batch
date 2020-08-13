import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

"""
database schema for book table
columns  -> id   title   author  price   year
types    -> int  str     str     float   int
property -> pk   unique  -       -       -
"""

# ORM table

class Book(Base): # inherit Base class function n property

    __tablename__ = 'books'  # table name must be plural and in small letter

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    author = Column(String)
    price = Column(Float)
    year = Column(Integer)


# create a class Game and then make a table
# create a class Employee and then add table code for ORM



if __name__ == "__main__": # if the file in run directly and not imported
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)
