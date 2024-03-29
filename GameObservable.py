from abc import ABCMeta, abstractmethod
import time

class GameObservable(metaclass=ABCMeta):

    def __init__(self):
        self.observers = []
        self.moveStrategyFactory = None
        self.winner = None

    def startTimer(self):
        self.startTime = time.time()

    def getTimerTotal(self):
        return (time.time() - self.startTime)/60

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
    def getWinner(self):
        pass

    @abstractmethod
    def setWinner(self):
        pass

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
