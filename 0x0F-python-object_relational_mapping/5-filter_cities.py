#!/usr/bin/python3
""" takes name of state as arg and lists all citiesof the state """

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            charset='utf8',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cur = db.cursor()
    cmd = "SELECT cities.name FROM cities JOIN states\
            ON cities.state_id = states.id WHERE states.name= %s"
    cur.execute(cmd, (sys.argv[4],))
    rows = cur.fetchall()
    my_list = []
    for row in rows:
        my_list.append(",".join(str(x) for x in row))
    print(*my_list, sep=", ")
    cur.close()
    db.close()
