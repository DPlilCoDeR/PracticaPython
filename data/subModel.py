import sqlite3
from sqlite3 import OperationalError, IntegrityError, ProgrammingError

ddbb_name = "prueba_bbdd2"


def connect_to_bbdd(bbdd=None):
    if bbdd is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
        return
    mydb = f'{bbdd}.db'
    print('New connection to SQLite DB...')
    connection = sqlite3.connect(mydb)
    return connection


def disconnect_bbdd(db=None, conn=None):
    if db is not ddbb_name:
        print("You are trying to disconnect from a wrong DB")
    if conn is not None:
        conn.close()


def connect(func):
    def inner_func(conn, *args, **kwargs):
        try:
            conn.execute(
                'SELECT name FROM sqlite_temp_master WHERE type="table";')
        except (AttributeError, ProgrammingError):
            conn = connect_to_bbdd(ddbb_name)
        return func(conn, *args, **kwargs)

    return inner_func


def scrub(input_string):
    return ''.join(k for k in input_string if k.isalnum())


@connect
def create_table(conn, table_name):
    table_name = scrub(table_name)
    sql = 'CREATE TABLE {} (USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,' \
          'NAME VARCHAR(20), LAST_NAME VARCHAR(20), PASSWORD VARCHAR(10), COMMENTS VARCHAR(50))'.format(table_name)
    try:
        conn.execute(sql)
    except OperationalError as e:
        print(e)


@connect
def insert_one(conn, name, last_name, password, comments, table_name):
    table_name = scrub(table_name)
    sql = "INSERT INTO {} ('NAME', 'LAST_NAME', 'PASSWORD', 'COMMENTS') VALUES (?, ?, ?, ?)" \
        .format(table_name)
    try:
        conn.execute(sql, (name, last_name, password, comments))
        conn.commit()
    except IntegrityError as e:
        print(e)


def tuple_to_dict(mytuple):
    mydict = dict()
    mydict['id'] = mytuple[0]
    mydict['name'] = mytuple[1]
    mydict['last_name'] = mytuple[2]
    mydict['password'] = mytuple[3]
    mydict['comments'] = mytuple[4]
    return mydict


@connect
def select_one(conn, user_id, table_name):
    table_name = scrub(table_name)
    user_id = scrub(user_id)
    sql = 'SELECT * FROM {} WHERE USER_ID="{}"'.format(table_name, user_id)
    c = conn.execute(sql)
    result = c.fetchone()
    return tuple_to_dict(result)


@connect
def update_one(conn, user_id, name, last_name, password, comments, table_name):
    table_name = scrub(table_name)
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE name=? LIMIT 1)' \
        .format(table_name)
    sql_update = 'UPDATE {} SET NAME=?, LAST_NAME=?, PASSWORD, COMMENTS, WHERE USER_ID=?' \
        .format(table_name)
    c = conn.execute(sql_check, (name,))  # we need the comma
    result = c.fetchone()
    if result[0]:
        c.execute(sql_update, (name, last_name, password, comments, user_id))
        conn.commit()


@connect
def delete_one(conn, user_id, table_name):
    table_name = scrub(table_name)
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE USER_ID=? LIMIT 1)' \
        .format(table_name)
    table_name = scrub(table_name)
    sql_delete = 'DELETE FROM {} WHERE USER_ID=?'.format(table_name)
    c = conn.execute(sql_check, (user_id,))  # we need the comma
    result = c.fetchone()
    if result[0]:
        c.execute(sql_delete, (user_id,))  # we need the comma
        conn.commit()
