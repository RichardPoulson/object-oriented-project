import pymysql
from interface import implements
from DBInterface import *

class DB(implements(DBInterface)):
    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='gbar')
        self.cursor = self.connection.cursor()

    def executeInsertionQuery(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def executeSelectionQuery(self, query):
        results = []
        self.cursor.execute(query)

        data = self.cursor.fetchone()
        while (data is not None):
            results.append(data)
            data = self.cursor.fetchone()

        return results
