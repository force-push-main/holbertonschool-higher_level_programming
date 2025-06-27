#!/usr/bin/python3
"""script that returns states with 'c' in name"""


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

    for state in (session.query(State.id, State.name)
                  .filter(State.name.contains("a"))):
        print(f"{state[0]}: {state[1]}")
