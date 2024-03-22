#!/usr/bin/python3
"""lists all states with a name starting with N"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], name=sys.argv[2])
    cursor =db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        if row[0][1] == 'N':
            print(row)

    cursor.close()

