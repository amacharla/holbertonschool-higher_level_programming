#!/usr/bin/python3
"""
Module with SQLAlchemy
Adds State and links it to City
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State, Base
    from relationship_city import City

    # open a connection
    engine = create_engine('mysql+mysqldb://'
                           '{0.argv[1]}:{0.argv[2]}@localhost/{0.argv[3]}'
                           .format(sys))

    # update tables before adding attr
    #Base.metadata.create_all(engine)
    # use connection
    Session = sessionmaker(bind=engine)
    session = Session()  # session instance

    ca = State(name='California')
    ca.cities= [City(name='San Francisco')]  # needs to be in list to add attr
    session.add(ca)
    session.commit()  # have to add it to sql in order to retrive autogen id
