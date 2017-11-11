#!/usr/bin/python3
""" retrieves all cities and states """

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    from model_city import City

    # open a connection
    engine = create_engine('mysql+mysqldb://'
                            '{0.argv[1]}:{0.argv[2]}@localhost/{0.argv[3]}'
                            .format(sys))
    # use connection
    Session = sessionmaker(bind=engine)
    session = Session()  # session instance

    # using join to retrieve city and state
    for city, state in session.query(City, State.name).join(State,
            State.id == City.state_id):
        print("{1}: ({0.id}) {0.name}".format(city, state))
