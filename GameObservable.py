from abc import ABCMeta, abstractmethod

class GameObservable(metaclass=ABCMeta):

    _observers = []

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

    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def setState(self, newState):
        pass

    @abstractmethod
    def initializeGameBoard(self):
        pass
