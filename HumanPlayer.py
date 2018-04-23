from Player import *
from CheckersPiece import *

class HumanPlayer(Player):
    def __init__(self, playerID=None):
        super(HumanPlayer, self).__init__()
        self.id = playerID

    def makeMove(self, gameBoard, pieceID, moveType):
        self.pieces[pieceID].movePiece(gameBoard, self, moveType)
