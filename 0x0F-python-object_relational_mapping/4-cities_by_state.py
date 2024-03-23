#!/usr/bin/python3
"""A script that lists all cities from the database"""

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
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states 
            ON cities.id  = states.id
            ORDER BY cities.id ASC"""

    cur.execute(query)

    results = cur.fetchall()

    for i in results:
        print(i)

    db.close()
