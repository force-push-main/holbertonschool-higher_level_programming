#!/usr/bin/python3
"""script that updateds a record into table"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, delete
    from sqlalchemy.orm import Session
    from model_state import State

    engine = create_engine(
        f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
        )
    session = Session(engine)
    stmt = (delete(State)
            .where(State.name.contains('a')))
    session.execute(stmt)
    session.commit()
