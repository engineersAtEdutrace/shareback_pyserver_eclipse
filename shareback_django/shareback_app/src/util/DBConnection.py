import mysql.connector as connection


class DBConnection:

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'my_schema',
            'raise_on_warnings': True,
        }
        self.conn = connection.connect(**config)

    def get_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def close(self):
        self.conn.close()

