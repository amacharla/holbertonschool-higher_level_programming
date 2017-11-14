#!/usr/bin/python3
""" Module with SQLAlchemy """

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey  # new attr
from relationship_state import Base


class City(Base):
    """ Creating a Table for 'cities' """
    __tablename__ = 'cities'  # name of table

    # column name = column attr
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
                                            # using foreign key
