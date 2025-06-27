#!/usr/bin/python3
"""script that lists all state objects from db"""

if __name__ == "__main__":
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State.id, State.name).order_by(State.id)
    if result != None:
        print(*(f"{row[0]}: {row[1]}" for row in result), sep='\n', end='\n')
