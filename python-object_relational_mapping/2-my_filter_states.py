#!/usr/bin/python3
"""Lists all states matching a name given as argument.

Warning: this script builds its query with str.format, so it is
vulnerable to SQL injection. See 3-my_safe_filter_states.py for the
injection-safe version.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = BINARY '{}' "
        "ORDER BY id ASC").format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
