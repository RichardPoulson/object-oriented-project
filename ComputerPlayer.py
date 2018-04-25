from Player import *
from CheckersPiece import *

class ComputerPlayer(Player):
    def __init__(self, playerID=None, aiStrategy=None):
        super(ComputerPlayer, self).__init__()
        self.id = playerID
        self.aiStrategy = aiStrategy

    def makeMove(self, gameBoard, pieceID, moveType):
        pieceID = 'O10'
        moveType = 'moveLeft'
        self.pieces[pieceID].movePiece(gameBoard, self, moveType)
