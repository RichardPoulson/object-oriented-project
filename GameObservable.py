class GameObservable:

    def __init__(self):
        self._observers = []
        self._address = None

    def addObserver(self, player):
        self._observers.append(player)

    def removeObserver(self, player):
        pass

    def notifyObservers(self):
        pass

    def getState(self):
        pass

    def setState(self):
        pass

    def resetState(self):
        pass
