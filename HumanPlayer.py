from AbstractPlayer import *

class HumanPlayer(AbstractPlayer):
    def __init__(self, playerID=None):
        self._id = playerID

    def makeMove(self, gameBoard, piece, moveType):
        piece.movePiece(gameBoard, self, moveType)
