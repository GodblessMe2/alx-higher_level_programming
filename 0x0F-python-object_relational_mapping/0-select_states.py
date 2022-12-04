#!/usr/bin/python3
"""  script that lists all states from the database hbtn_0e_0_usa: """

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            charset='utf8'
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for r in rows:
        print("({}, '{}')".format(r[0], r[1]))

    cur.close()
    db.close()
