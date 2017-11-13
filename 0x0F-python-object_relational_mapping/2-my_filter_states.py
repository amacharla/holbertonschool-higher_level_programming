#!/usr/bin/python3
"""
List all states based of given 4th argument
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    # for substitution, need to use '%' and needs to be in tupile even for one
    cur.execute("SELECT * FROM states WHERE name='{:s}' ORDER BY id ASC".format(sys.argv[4]))
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
    db.close()
