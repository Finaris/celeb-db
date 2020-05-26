# -*- coding: utf-8 -*-
"""

Defines the database that stores celebrities.

"""

import sqlite3


def create_connection(db_file):
    """ creates a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """


if __name__ == "__main__":
    create_connection("celeb.db")
