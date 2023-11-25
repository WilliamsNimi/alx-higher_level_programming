#!/usr/bin/python3
""" Python module for MYSQLdb Library """
import MySQLdb
import sys

def database_access(user, pword, database):
    """
    Accessing the holberton DB via this function
    """
db = MySQLdb.connect(user=user, passwd=pword, db=database, host="localhost", port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in cur.fetchall():
    print(row)

if __name__ == "__main__":
    database_access(sys.argv[1], sys.argv[2], sys.argv[3])
