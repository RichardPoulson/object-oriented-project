from Player import *
from CheckersPiece import *

class HumanPlayer(Player):
    def __init__(self, playerID=None):
        self._id = playerID
        self._pieces = {}
        self._numPieces = 0

    def addToPieceCollection(self, newPieceID, newPiece):
        self._pieces[newPieceID] = newPiece

    def getPieceFromCollection(self, pieceID):
        return self._pieces[pieceID]

    def getNumPieces(self):
        return self._numPieces

    def setNumPieces(self):
        self._numPieces = len(self._pieces)

    def decrementNumPieces(self):
        self._numPieces -= 1

    def makeMove(self, gameBoard, pieceID, moveType):
        self._pieces[pieceID].movePiece(gameBoard, self, moveType)

    def update(self, gameState):
        gameState.printBoard()
