#!/usr/bin/python3
"""script that lists all state objects from db"""

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

url = f"mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
result = session.query(State.id, State.name).order_by(State.id)

print(f"{row.id}: {row.name}" for row in result)
