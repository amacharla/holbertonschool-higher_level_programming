#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of that state
"""

if __name__ == "__main__":
    import MySQLdb, sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    # for substitution, need to use '%' and needs to be in tupile even for one
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s ORDER BY cities.id ASC", [sys.argv[4]])
    result = [city for cities in cur.fetchall() for city in cities]
    print(', '.join(result))
    cur.close()
    db.close()
