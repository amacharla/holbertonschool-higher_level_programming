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

    # find row with id 2
    row = session.query(State).filter(State.id == 2).first()
    row.name = "New Mexico"  # update name
    session.commit()  # push chances into database
