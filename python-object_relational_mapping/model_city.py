#!/usr/bin/python3
"""class with a model for the city table"""


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """city class"""
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
