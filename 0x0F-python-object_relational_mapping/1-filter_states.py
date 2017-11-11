#!/usr/bin/python3
"""
list all states with a name starting with N (upper N)
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
#            , host=localhost, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
    db.close()
