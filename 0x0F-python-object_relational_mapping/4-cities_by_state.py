#!/usr/bin/python3
"""
List all cities with respective states from two different tables
"""

if __name__ == "__main__":
    import MySQLdb, sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id=states.id ORDER BY id ASC")
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
    db.close()
