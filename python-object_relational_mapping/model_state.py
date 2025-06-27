#!/usr/bin/python3
"""class with a model for the states stable"""


from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# engine = create_engine("mysql://root:root@localhost/hbtn_0e_6_usa")
# Base.metadata.create_all(engine)


class State(Base):
    """State class"""
    __table__name = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128))
