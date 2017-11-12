#!/usr/bin/python3
""" Module with SQLAlchemy """

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    # open a connection
    engine = create_engine('mysql+mysqldb://'
                           '{0.argv[1]}:{0.argv[2]}@localhost/{0.argv[3]}'
                           .format(sys))
    # use connection
    Session = sessionmaker(bind=engine)
    session = Session()  # session instance

    # retrieve only one withe the `first()`
    state_name = sys.argv[4]
    try:
        state = session.query(State).filter(State.name == sys.argv[4]).one()
    except Exception:
        print("Not found")
    else:
        print(state.id)
