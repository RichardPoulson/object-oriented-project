import pymysql
from interface import implements
from DBInterface import *

class DB(implements(DBInterface)):
    def __init__(self):

        self.insertionQueryDictionary = {

        }

        self.selectionQueryDictionary = {
            'ranks': "SELECT username, wins, losses FROM users ORDER BY wins DESC;",
            'playTime': "SELECT 'TOTAL' AS 'user', SUM(playtime) AS 'PlayTime' from users UNION SELECT username AS 'user', playtime AS 'PlayTime' FROM users ORDER BY playtime DESC;"
        }

        self.updateQueryDictionary = {
            'wins': "UPDATE users SET wins=wins+{} WHERE username=\'{}\';",
            'losses': "UPDATE users SET losses=losses+{} WHERE username=\'{}\';",
            'playtime': "UPDATE users SET playtime=playtime+{} WHERE username=\'{}\';"
        }

        try:
            self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='gbar')
            self.cursor = self.connection.cursor()
        except pymysql.err.OperationalError:
            self.connection = None
            self.cursor = None


    def executeInsertionQuery(self, queryKey):
        if (self.connection is not None) and (self.cursor is not None):
            try:
                self.cursor.execute(self.insertionQueryDictionary[queryKey])
                self.connection.commit()
            except pymysql.err.ProgrammingError:
                pass

    def executeSelectionQuery(self, queryKey):
        if (self.connection is not None) and (self.cursor is not None):
            results = []
            try:
                self.cursor.execute(self.selectionQueryDictionary[queryKey])

                data = self.cursor.fetchone()
                while (data is not None):
                    results.append(data)
                    data = self.cursor.fetchone()

            except pymysql.err.ProgrammingError:
                pass

            return results

    def executeUpdateQuery(self, queryKey, user, value):
        if (self.connection is not None) and (self.cursor is not None):
            try:
                self.cursor.execute(self.updateQueryDictionary[queryKey].format(value, user.getUsername()))
                self.connection.commit()
            except pymysql.err.ProgrammingError:
                pass
