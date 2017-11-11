#!/usr/bin/python3
"""
List all the states
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
    db.close()
