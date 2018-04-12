from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    pieces = {}
    currentGameState = None

    def addToPieceCollection(self, newPieceID, newPiece):
        self.pieces[newPieceID] = newPiece

    def getPieceFromCollection(self, pieceID):
        return self.pieces[pieceID]

    @abstractmethod
    def getPlayerPieces(self):
        pass

    @abstractmethod
    def makeMove(self, gameBoard, pieceID, moveType):
        pass

    @abstractmethod
    def update(self, gameBoard):
        pass
