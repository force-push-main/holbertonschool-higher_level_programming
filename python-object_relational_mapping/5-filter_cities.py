#!/usr/bin/python3

"""script that returns cities from state"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )
    c = db.cursor()

    c.execute(
        """SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (sys.argv[4], )
    )

    rows = c.fetchall()
    print(*(row[0] for row in rows), sep=", ")
