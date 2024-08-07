#!/usr/bin/python3
"""states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    state_name = sys.argv[4] #
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
 '{}' ORDER BY id ASC".format(state_name))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
