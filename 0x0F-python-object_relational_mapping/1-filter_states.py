#!/usr/bin/python3
"""A script that lists all states with a name starting with N """


import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    results = cur.fetchall()

    cities = []
    for i in results:
        if i[1][0] == "N":
            print(i)
    db.close()
