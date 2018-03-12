class GameObservable:

    def __init__(self):
        self._observers = []
        self._address = None

    def addObserver(self, player):
        self._observers.append(player)

    def removeObserver(self, player):
        try:
            self._observers.remove(player)
        except ValueError:
            return

    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self)

    def getState(self):
        pass

    def setState(self):
        pass

    def resetState(self):
        pass
