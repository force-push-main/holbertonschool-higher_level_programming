#!/usr/bin/python3
"""script that lists all state objects from db"""

if __name__ == "__main__":
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    url = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)

    print(result)

    # *(f"{row.id}: {row.name}" for row in result)
