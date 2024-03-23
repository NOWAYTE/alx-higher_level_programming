#!/usr/bin/python3
"""A script that takes in an argument and displays allment """

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states".format(sys.argv[4]).strip("'"))

    result = cur.fetchall()

    for i in result:
        print(i)

    db.close()
