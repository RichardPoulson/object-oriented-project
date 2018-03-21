from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    _pieces = {}

    @abstractmethod
    def update(self, gameState):
        pass

    @abstractmethod
    def makeMove(self, gameBoard, pieceID, moveType):
        pass
