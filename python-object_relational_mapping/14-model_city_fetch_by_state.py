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
    results = (session.query(City, State)
               .join(State, City.state_id == State.id)
               .order_by(City.id))
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
