#!/usr/bin/python3
"""a script that returns a joined table"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, join, select
    from sqlalchemy.orm import Session
    from model_city import City
    from model_state import State

    engine = create_engine(
        f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
        )
    session = Session(engine)
    stmt = select(City).join(State, City.state_id == State.id)
    results = session.execute(stmt)
    for row in results:
        print(f"{row.name}: ({row.id}) {row.name}")
