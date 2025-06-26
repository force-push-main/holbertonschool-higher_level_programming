#!/usr/bin/python3

"""python script to get states from db using ORM"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3]
        )
    c = db.cursor()
    c.execute("""SELECT *
              FROM cities
              ORDER BY cities.id ASC"""
              )
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
