from interface import Interface

class DBInterface(Interface):
    def executeInsertionQuery(self, queryKey):
        pass

    def executeSelectionQuery(self, query):
        pass

    def executeUpdateQuery(self, queryKey, user, value):
        pass
