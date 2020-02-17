import mysql.connector

from flask import g


def init_db():
    print("Initialization")
    db = get_db().cursor()

    try:
        print("Dropping table if exists")
        db.execute("""DROP TABLE IF EXISTS user;""")
        print("Creating User Table")
        db.execute("""CREATE TABLE user ( 
                             Id int(11) NOT NULL,
                             name varchar(250) NOT NULL,
                             password varchar(250) NOT NULL,
                             PRIMARY KEY (Id));""")
        print("Initializing User Table")
        db.execute("""INSERT INTO user (Id, name, password) 
                           VALUES 
                           (1, 'name', "password") """)
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))

    # with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r') as f:
    #     db.execute(f.read())


    # resultset = cursor.fetchall()
    # for user in resultset:
    #     print(tuple(user))
    #
    # db.execute(
    #     'INSERT INTO user (username, password) VALUES (?, ?)',
    #     ("root", "toor")
    # )
    #
    # db.execute(
    #     'INSERT INTO user (username, password) VALUES (?, ?)',
    #     ("username2", "password2")
    # )
    #
    # db.commit()


def get_users():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM user;")
    resultset = cursor.fetchall()
    print("Getting results")
    for user in resultset:
        print(tuple(user))


def get_db():
    config = {
        # 'user': os.environ.get("username"),
        # 'password': os.environ.get("password"),
        # 'host': os.environ.get("hostname"),
        # 'database': os.environ.get("name"),
        # 'raise_on_warnings': True
        'user': 'b46940c5b20663',
        'password': '62d0dde5',
        'host': 'us-cdbr-iron-east-04.cleardb.net',
        'database': 'ad_b4f194586b2f30d',
        'raise_on_warnings': True
    }


    if 'db' not in g:
        # Check if Local Development
        #g.db = sqlite3.connect(
        #    "app/db/mydatabase.db"
        #)
        #g.db.row_factory = sqlite3.Row
        g.db = mysql.connector.connect(**config)


    return g.db
