#!/usr/bin/python3
"""A script that takes name of a states as an argument and lists cities """

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

    cur.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    results = cur.fetchall()

    for i in results:
        print(i)

