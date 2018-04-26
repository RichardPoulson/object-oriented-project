from Player import *
from CheckersPiece import *
from CheckersHeuristic import *
from AlphaBetaSearch import *
from random import shuffle

class ComputerPlayer(Player):
    def __init__(self, playerID=None):
        super(ComputerPlayer, self).__init__()
        self.id = playerID
        self.heuristic = None
        self.aiStrategy = None

    def setHeuristic(self, game):
        self.heuristic = CheckersHeuristic(game, self)

    def initializeAIStrategy(self):
        self.aiStrategy = AlphaBetaSearch(self.heuristic.getCheckersBoard(), self.heuristic)

    def makeMove(self, gameBoard, pieceID, moveType):
        if self.aiStrategy is not None:
            (pieceToMove, moveType) = self.aiStrategy.search(gameBoard, 2)
        else:
            moveOptions = gameBoard.getAvailableMoves()
            shuffle(moveOptions)
            for piece, move in moveOptions:
                if piece.ID.startswith('O'):
                    pieceToMove = piece
                    moveType = move
                    break

        self.pieces[pieceToMove.ID].movePiece(gameBoard, self, moveType)
