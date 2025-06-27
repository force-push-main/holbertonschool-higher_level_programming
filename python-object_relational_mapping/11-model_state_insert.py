#!/usr/bin/python3
"""script that inserts new record into table"""


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
    Louisiana = State(name='Louisiana')
    session.add(Louisiana)
    session.commit()
    result = (session.query(State.id)
              .filter(State.name == "Louisiana")).first()
    print(result[0])
