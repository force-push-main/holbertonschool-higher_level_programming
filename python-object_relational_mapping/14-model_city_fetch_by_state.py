#!/usr/bin/python3
"""a script that returns a joined table"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_city import City
    from model_state import State

    engine = create_engine(
        f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
        )
    session = Session(engine)
    results = session.query(City).join(State).all()
    for row in results:
        print(row)
