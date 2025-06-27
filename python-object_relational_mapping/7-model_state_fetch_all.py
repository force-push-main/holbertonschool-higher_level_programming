#!/usr/bin/python3
"""script that lists all state objects from db"""

from model_state import Base, State
from sqlalchemy import create_engine
import sys

url = f"mysql+mysqldb://{sys[1]}:{sys[2]}@localhost/{sys[3]}" 
engine = create_engine(url)
c = engine.connect()
result = c.execute("SELECT id, name FROM State SORT BY id ASC")

print(result.fetchall())
