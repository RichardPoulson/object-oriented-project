from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    _pieces = {}

    def addToPieceCollection(self, newPieceID, newPiece):
        self._pieces[newPieceID] = newPiece

    def getPieceFromCollection(self, pieceID):
        return self._pieces[pieceID]

    @abstractmethod
    def update(self, gameState):
        pass

    @abstractmethod
    def makeMove(self, gameBoard, pieceID, moveType):
        pass
