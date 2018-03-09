from GameObservable import *
from PieceFactory import *
from Space import *
from PieceFactory import *

class CheckersBoard(GameObservable):

    def __init__(self):
        self._pieceFactory = PieceFactory()
        self.player1Pieces = [None for pieceNumber in range(0, 12)]
        self.player2Pieces = [self._pieceFactory.getPiece(pieceOwner='O') for pieceNumber in range(0, 12)]
        self.spaces = [[Space(locationY=j, locationX=i) for i in range(0, 8)] for j in range(0, 8)]

    def initializeGameBoard(self):
        pieceCounter = 0
        for i in range(0, 3):
            for j in range(0, len(self.spaces), 2):
                if ((i % 2) == 0):
                    self.player1Pieces[pieceCounter] = self._pieceFactory.getPiece(pieceOwner='X{}'.format(pieceCounter), pieceLocation=self.spaces[i][j+1])
                    self.player2Pieces[pieceCounter] = self._pieceFactory.getPiece(pieceOwner='O{}'.format(pieceCounter), pieceLocation=self.spaces[7-i][j])
                    self.spaces[i][j+1].setSpaceOwner(self.player1Pieces[pieceCounter])
                    self.spaces[7-i][j].setSpaceOwner(self.player2Pieces[pieceCounter])
                else:
                    self.player1Pieces[pieceCounter] = self._pieceFactory.getPiece(pieceOwner='X{}'.format(pieceCounter), pieceLocation=self.spaces[i][j])
                    self.player2Pieces[pieceCounter] = self._pieceFactory.getPiece(pieceOwner='O{}'.format(pieceCounter), pieceLocation=self.spaces[7-i][j+1])
                    self.spaces[i][j].setSpaceOwner(self.player1Pieces[pieceCounter])
                    self.spaces[7-i][j+1].setSpaceOwner(self.player2Pieces[pieceCounter])
                pieceCounter += 1

    def getState(self):
        pass

    def setState(self):
        pass

    def getSpaceByLocation(self, i, j):
        returnSpace = None
        if (i >= 0 and j < len(self.spaces)) and (i >= 0 and j < len(self.spaces[0])):
            returnSpace = self.spaces[i][j]
        return returnSpace

    def makePlayer1Move(self, piece, moveType):
        piece.movePiece(self, moveType.rowChange, moveType.columnChange)

    def makePlayer2Move(self, moveType):
        piece.movePiece(self, moveType.rowChange, moveType.columnChange)

    #for testing
    def printBoard(self):
        for row in self.spaces:
            print(['--' if (space.getSpaceOwner() is None) else space.getSpaceOwner()._owner for space in row])
