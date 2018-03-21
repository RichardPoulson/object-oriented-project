from Player import *
from CheckersPiece import *

class HumanPlayer(Player):
    def __init__(self, playerID=None):
        self.id = playerID
        self.pieces = {}
        self.numPieces = 0

    def getNumPieces(self):
        return self.numPieces

    def setNumPieces(self):
        self.numPieces = len(self.pieces)

    def decrementNumPieces(self):
        self.numPieces -= 1

    def makeMove(self, gameBoard, pieceID, moveType):
        self.pieces[pieceID].movePiece(gameBoard, self, moveType)

    def update(self, gameState):
        gameState.printBoard()
