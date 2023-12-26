#!/usr/bin/python3
""" Python module for MYSQLdb Library """
import MySQLdb
import sys


def database_access(u, pw, db, s):
    """
    Accessing the holberton DB via this function
    """
    db = MySQLdb.connect(user=u, passwd=pw, db=db, host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT c.name FROM cities c \
JOIN states s ON c.state_id=s.id WHERE s.name={} ORDER BY c.id ASC".format(s))
    rows = cur.fetchall()
    results = ''
    for i in range(len(rows)):
        if i == len(rows) - 1:
            results += rows[i][0]
        else:
            results += rows[i][0] + ', '
    print(results)


if __name__ == "__main__":
    database_access(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
