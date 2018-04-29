from interface import implements
from DBInterface import *

class DBProxy(implements(DBInterface)):
    def __init__(self, DB):
        self.realDB = DB

    def getRealDB(self):
        return self.realDB

    def setRealDB(self, DB):
        self.realDB = DB

    def executeInsertionQuery(self, query):
        self.getRealDB().executeInsertionQuery(query)

    def executeSelectionQuery(self, query):
        return self.getRealDB().executeSelectionQuery(query)

    def executeUpdateQuery(self, queryKey, user, value):
        return self.getRealDB().executeUpdateQuery(queryKey, user, value)
