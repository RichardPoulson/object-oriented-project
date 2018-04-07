import pymysql
from interface import implements
from DBInterface import *

class DB(implements(DBInterface)):
    def __init__(self):
        self.connection = pymysql.connect(host='sql3.freemysqlhosting.net', user='sql3231332', password='TfzATskluT', db='sql3231332')
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
