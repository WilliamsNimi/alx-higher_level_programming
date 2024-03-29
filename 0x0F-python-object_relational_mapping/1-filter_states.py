#!/usr/bin/python3
""" Python module for MYSQLdb Library """
import MySQLdb
import sys


def database_access(u, pw, db):
    """
    Accessing the holberton DB via this function
    """
    db = MySQLdb.connect(user=u, passwd=pw, db=db, host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    database_access(sys.argv[1], sys.argv[2], sys.argv[3])
