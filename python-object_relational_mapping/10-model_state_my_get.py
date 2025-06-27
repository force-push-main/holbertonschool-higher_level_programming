#!/usr/bin/python3
"""script that prints state id from search param"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    engine = create_engine(
        f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    result = (session.query(State.id)
              .filter(State.name == sys.argv[4]))
    if result is not None:
        print(result[0])
    else:
        print("Not found")
