from AbstractPlayer import *

class HumanPlayer(AbstractPlayer):
    def __init__(self, playerID=None):
        self._id = playerID
        self._numPieces = 0

    def makeMove(self, gameBoard, piece, moveType):
        piece.movePiece(gameBoard, self, moveType)
        gameBoard.notifyObservers()

    def update(self, gameBoard):
        gameBoard.printBoard()
