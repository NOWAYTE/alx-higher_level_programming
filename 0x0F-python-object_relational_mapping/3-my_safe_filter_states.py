#!/usr/bin/python3
"""
    A script that takes in an argument and displays values alike in the states

    """

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    results = cur.fetchall()

    for i in results:
        if i[1] == sys.argv[4]:
            print(i)

    db.close()
