# Created by rajesh.sahoo at 12:56 2020-06-21
import sqlite3
from django import db

db.connections.close_all()

from django.conf import settings

db_file = "{}/db.sqlite3".format(settings.BASE_DIR)


def select_all_tasks(query):
    """
    Query all rows in the tasks table
    :param db_file: database file; query: select query;
    :return:
    """
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(query)
    headers = tuple(map(lambda x: x[0], cur.description))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [headers] + rows


def insert_data_into_table(table_name, column_names, values):
    conn = sqlite3.connect(db_file)
    sql = ''' INSERT or REPLACE INTO {}({})
                  VALUES({}) '''.format(table_name, ','.join(column_names), ','.join(['?'] * len(column_names)))
    cur = conn.cursor()
    affected_rows = 0

    for val in values:
        cur.execute(sql, val)
        affected_rows += cur.rowcount

    conn.commit()
    conn.close()

    return affected_rows


def TruncateTableData(table_name):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute('DELETE FROM {};'.format(table_name))
    conn.commit()
    conn.close()
    return True
