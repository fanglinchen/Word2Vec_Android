import configparser

import MySQLdb

parser = configparser.ConfigParser()
parser.read('settings.ini')


class DBConnector:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host=parser.get('DATABASE', 'HOST'),
            user=parser.get('DATABASE', 'USER'),
            password=parser.get('DATABASE', 'PASSWORD'),
            db=parser.get('DATABASE', 'DB'),
            use_unicode=True,
            charset="utf8")
        self.conn.set_character_set('utf8mb4')
        self.conn.autocommit(on=False)
        self.cursor = self.conn.cursor()

    def get_cursor(self):
        return self.cursor

    def get_connection(self):
        return self.conn