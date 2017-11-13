#!/usr/bin/python3
"""
List all Relationships for states
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

    # use connection
    Session = sessionmaker(bind=engine)
    session = Session()  # session instance

    allstates = session.query(State).all()

    for state in allstates:
        print("{0.id}: {0.name}".format(state))
        for city in state.cities:
            print("\t{0.id}: {0.name}".format(city))

    session.close()
