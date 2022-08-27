import typing as t
from mysql.connector import connect, MySQLConnection
from config import db_config

def get_db_cnx() -> MySQLConnection:
    try: 
        return connect(**db_config)
    except Exception as e:
        print('Oops unable to establish a connection: ' + str(e))
