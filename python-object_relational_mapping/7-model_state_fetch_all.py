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
    for row in session.query(State.id, State.name).order_by(State.id):
        print(row)

    # (f"{row.id}: {row.name}" for row in result)
