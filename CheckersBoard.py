from GameObservable import *
from PieceFactory import *
from Space import *
from PieceFactory import *

class CheckersBoard(GameObservable):

    def __init__(self):
        self._pieceFactory = PieceFactory()
        self.player1Pieces = [self._pieceFactory.getPiece(pieceOwner='X')]*10
        self.player2Pieces = [self._pieceFactory.getPiece(pieceOwner='O')]*10
        # TODO: error here. In defining the matrix below, the same instance of Space is used for each element
        self.spaces = [[Space()]*8]*8

    def initializeGameBoard(self):
        pass
    #    for i in range(0, 3):
    #        for j in range(0, len(self.spaces), 2):
    #            self.spaces[0][0].setSpaceOwner(self.player1Pieces[0])

    def getState(self):
        pass

    def setState(self):
        pass

    #for testing
    def printBoard(self):
        for row in self.spaces:
            print([space.icon if (space.getSpaceOwner() is None) else space.getSpaceOwner()._owner for space in row])
