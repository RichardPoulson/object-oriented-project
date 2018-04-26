from Player import *
from CheckersPiece import *
from CheckersHeuristic import *
from AlphaBetaSearch import *

class ComputerPlayer(Player):
    def __init__(self, playerID=None):
        super(ComputerPlayer, self).__init__()
        self.id = playerID
        self.heuristic = None
        self.aiStrategy = None

    def setHeuristic(self, game):
        self.heuristic = CheckersHeuristic(game, self)

    def setAIStrategy(self, game):
        self.aiStrategy = AlphaBetaSearch(game, self.heuristic)

    def makeMove(self, gameBoard, pieceID, moveType):
        if self.aiStrategy is not None:
            (pieceToMove, moveType) = self.aiStrategy.search(gameBoard, 2)
            print(pieceToMove.ID)
        else:
            #assign Random Move
            pass

        self.pieces[pieceToMove.ID].movePiece(gameBoard, self, moveType)
