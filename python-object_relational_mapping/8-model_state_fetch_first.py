#!/usr/bin/python3
"""script that returns first result from db"""


if __name__ == "__main__":
    import sys
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id, State.name).first()
    if result != None:
        print(f"{result[0]}: {result[1]}")
