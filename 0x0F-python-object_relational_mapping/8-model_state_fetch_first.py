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
    first = session.query(State).order_by(State.id).first()
    if first is not None:
        print("{0.id}: {0.name}".format(first))
    else: # if no table: states exist
        print("Nothing")
