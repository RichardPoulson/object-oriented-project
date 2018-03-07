from GameObservable import *
from PieceFactory import *
from Space import *
from PieceFactory import *

class CheckersBoard(GameObservable):

    def __init__(self):
        self._pieceFactory = PieceFactory()
        self.player1Pieces = [self._pieceFactory.getPiece(pieceOwner='X') for pieceNumber in range(0, 10)]
        self.player2Pieces = [self._pieceFactory.getPiece(pieceOwner='O') for pieceNumber in range(0, 10)]
        self.spaces = [[Space() for i in range(0, 8)] for j in range(0, 8)]

    def initializeGameBoard(self):
        for i in range(0, 3):
            for j in range(0, len(self.spaces), 2):
                if ((i % 2) == 0):
                    self.spaces[i][j+1].setSpaceOwner(self.player1Pieces[0])
                    self.spaces[7-i][j].setSpaceOwner(self.player2Pieces[0])
                else:
                    self.spaces[i][j].setSpaceOwner(self.player1Pieces[0])
                    self.spaces[7-i][j+1].setSpaceOwner(self.player2Pieces[0])

    def getState(self):
        pass

    def setState(self):
        pass

    #for testing
    def printBoard(self):
        for row in self.spaces:
            print(['-' if (space.getSpaceOwner() is None) else space.getSpaceOwner()._owner for space in row])
