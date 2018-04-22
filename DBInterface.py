from interface import Interface

class DBInterface(Interface):
    def executeInsertionQuery(self, queryKey):
        pass

    def executeSelectionQuery(self, queryKey):
        pass

    def executeUpdateQuery(self, queryKey, user, value):
        pass
