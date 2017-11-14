#!/usr/bin/python3
"""Module with SQLAlchemy"""

from sqlalchemy.ext.declarative import declarative_base  # base constructor
from sqlalchemy import Column, Integer, String

# construct `Base` from sqlalchemy
Base = declarative_base()


class State(Base):
    """ Creating a Table for 'states' """
    __tablename__ = 'states'  # name of table

    # column name = column attr
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
