from abc import ABCMeta, abstractmethod

class GameObservable(metaclass=ABCMeta):

    def __init__(self):
        self.observers = []
        self.moveStrategyFactory = None

    def addObserver(self, player):
        self.observers.append(player)

    def removeObserver(self, player):
        try:
            self.observers.remove(player)
        except ValueError:
            return

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self)

    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def setState(self, newState):
        pass

    @abstractmethod
    def initializeGameBoard(self, player1, player2):
        pass

    @abstractmethod
    def getReadOnlyState(self):
        pass
