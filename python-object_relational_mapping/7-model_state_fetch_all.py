#!/usr/bin/python3
"""script that lists all state objects from db"""

# if __name__ == "__main__":
#     from model_state import State
#     from sqlalchemy import create_engine
#     from sqlalchemy.orm import sessionmaker
#     import sys

#     url = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
#     engine = create_engine(url, pool_pre_ping=True)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     for row in session.query(State).order_by(State.id):
#         print(row)

#     # *(f"{row.id}: {row.name}" for row in result)

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
