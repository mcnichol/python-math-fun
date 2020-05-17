import json
import os
import sqlite3

import mysql.connector
from flask import g

DB_PROFILE = 'local'

if os.environ.get("VCAP_SERVICES") is not None:
    DB_PROFILE = 'cloud'


def init_db():
    print("Initialization")
    db = get_db()
    cursor = db.cursor()

    try:
        print("Dropping table if exists")
        cursor.execute("""DROP TABLE IF EXISTS message;""")
        db.commit()
    except mysql.connector.Error as err:
        print("No Need to drop, Table doesn't exist: {}".format(err))

    try:
        print("Creating Message Table")

        if DB_PROFILE == 'cloud':
            print("Connecting to MySQL")
            mysql_table = """CREATE TABLE message (
                                 Id int(11) NOT NULL AUTO_INCREMENT,
                                 message varchar(250) NOT NULL,
                                 PRIMARY KEY (Id));"""
            cursor.execute(mysql_table)
            db.commit()
        else:
            print("Connecting to local db")
            sqlite_table = """CREATE TABLE message (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
            """
            cursor.execute(sqlite_table)
            db.commit()
    except Exception as e:
        print("Failed creating table: {}".format(e))

    try:
        print("Initializing Message Table")
        cursor.execute("""INSERT INTO message (message) VALUES ('World') """)
        db.commit()
    except mysql.connector.Error as err:
        print("Failed inserting into table: {}".format(err))


def get_message():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM message;")
    resultset = cursor.fetchall()
    print("Returning {} result(s)".format(len(resultset)))
    return resultset


def get_db():
    if 'db' not in g:

        if DB_PROFILE == 'cloud':
            services = os.environ.get("VCAP_SERVICES")
            json_services = json.loads(services)
            credentials = json_services["cleardb"][0]["credentials"]

            config = {
                'user': credentials["username"],
                'password': credentials["password"],
                'host': credentials["hostname"],
                'database': credentials["name"],
            }
            g.db = mysql.connector.connect(**config)

        else:
            print("Running Local Database")
            g.db = sqlite3.connect("mydb.db")

    return g.db


def update_message(update_msg):
    print(update_msg)
    db = get_db()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO message (message) VALUES ('{update_msg}')")
    db.commit()

    return True
