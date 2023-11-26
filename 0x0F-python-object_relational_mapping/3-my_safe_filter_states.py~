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
    c.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(s))
    for row in c.fetchall():
        print(row)


if __name__ == "__main__":
    database_access(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
