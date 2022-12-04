#!/usr/bin/python3
""" lists all cities """

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      charset='utf8',
      user=sys.argv[1],
      passwd=sys.argv[2],
      db=sys.argv[3]
    )

    cur = db.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
