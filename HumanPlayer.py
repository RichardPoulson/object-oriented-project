from AbstractPlayer import *
from CheckersPiece import *

class HumanPlayer(AbstractPlayer):
    def __init__(self, playerID=None):
        self._id = playerID
        self._pieces = {}
        self._numPieces = 0

    def addToPieceCollection(self, newPieceID, newPiece):
        self._pieces[newPieceID] = newPiece

    def getPieceFromCollection(self, pieceID):
        return self._pieces[pieceID]

    def makeMove(self, gameBoard, pieceID, moveType):
        self._pieces[pieceID].movePiece(gameBoard, self, moveType)
        gameBoard.notifyObservers()

    def update(self, gameBoard):
        gameBoard.printBoard()
