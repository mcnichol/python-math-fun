import mysql.connector
from mysql.connector import Error

#"uri": ""

def connect():
    print("Do work")
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect("mysql://b46940c5b20663:62d0dde5@us-cdbr-iron-east-04.cleardb.net:3306/ad_b4f194586b2f30d?reconnect=true")
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
 
 
if __name__ == '__main__':
    connect()
