from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    pieces = {}

    def addToPieceCollection(self, newPieceID, newPiece):
        self.pieces[newPieceID] = newPiece

    def getPieceFromCollection(self, pieceID):
        return self.pieces[pieceID]

    @abstractmethod
    def update(self, gameState):
        pass

    @abstractmethod
    def makeMove(self, gameBoard, pieceID, moveType):
        pass
