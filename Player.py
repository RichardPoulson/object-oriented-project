from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    def __init__(self):
        self.pieces = {}
        self.numPieces = 0
        self.currentGameState = None

    def addToPieceCollection(self, newPieceID, newPiece):
        self.pieces[newPieceID] = newPiece

    def getPieceFromCollection(self, pieceID):
        return self.pieces[pieceID]

    def getPlayerPieces(self):
        return [piece for pieceID, piece in self.pieces.items()]

    def getNumPieces(self):
        return self.numPieces

    def setNumPieces(self):
        self.numPieces = len(self.pieces)

    def decrementNumPieces(self):
        self.numPieces -= 1

    def update(self, gameBoard):
        self.currentGameState = gameBoard

    @abstractmethod
    def makeMove(self, gameBoard, pieceID, moveType):
        pass
