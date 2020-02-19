import mysql.connector
from mysql.connector import Error, errorcode


def connect():
    print("Do work")
    """ Connect to MySQL database """
    conn = None
    config = {
        'user': "b46940c5b20663",
        'password': "62d0dde5", 'host': "us-cdbr-iron-east-04.cleardb.net", 'database': "ad_b4f194586b2f30d"
    }

    TABLES = {}
    TABLES['message'] = (
        "CREATE TABLE `message` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `message` varchar(200) NOT NULL,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB")

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        if conn.is_connected():
            print('Connected to MySQL database')
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name))
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
        else:
            print("OK")
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
