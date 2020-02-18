import os
import mysql.connector
import json

from flask import g


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
        cursor.execute("""CREATE TABLE message ( 
                             Id int(11) NOT NULL AUTO_INCREMENT,
                             message varchar(250) NOT NULL,
                             PRIMARY KEY (Id));""")
        db.commit()
    except mysql.connector.Error as err:
        print("Failed creating table: {}".format(err))

    try:
        print("Initializing Message Table")
        cursor.execute("""INSERT INTO message (message) VALUES ('Michael') """)
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

    config = {
        'user': 'b46940c5b20663',
        'password': '62d0dde5',
        'host': 'us-cdbr-iron-east-04.cleardb.net',
        'database': 'ad_b4f194586b2f30d',
        'raise_on_warnings': True
    }

    if 'db' not in g:
        g.db = mysql.connector.connect(**config)

    return g.db


def update_message(update_msg):
    print(update_msg)
    db = get_db()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO message (message) VALUES ('{update_msg}')")
    db.commit()

    return True
