from GameObservable import *
from PieceFactory import *
from Space import *
from PieceFactory import *
import numpy as np

class CheckersBoard(GameObservable):

    def __init__(self):
        super().__init__()
        self._pieceFactory = PieceFactory()
        self.playerPieces = []
        self.numRows = 8
        self.numCols = 8
        self.spaces = [[Space(locationJ=j, locationI=i) for i in range(0, self.numCols)] for j in range(0, self.numRows)]
        self.moveOptions = [{'moveLeft':(1,1), 'moveRight':(1,-1), 'jumpLeft':(2,2), 'jumpRight':(2,-2)}, {'moveLeft':(-1,-1), 'moveRight':(-1,1), 'jumpLeft':(-2,-2), 'jumpRight':(-2,2)}]

    def addObserver(self, player):
        super().addObserver(player)
        self.playerPieces.append([None for pieceNumber in range(0, 12)])


    def initializeGameBoard(self):
        assert (len(self._observers) == 2), 'Must have two players to start game'
        pieceCounter = 0
        for i in range(0, 3):
            for j in range(0, len(self.spaces), 2):
                if ((i % 2) == 0):
                    # initialize player1 pieces for even rows
                    self.playerPieces[0][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='X{0:02d}'.format(pieceCounter), pieceLocation=(i, j+1))
                    self.spaces[i][j+1].setSpaceOwner(self.playerPieces[0][pieceCounter])

                    # initialize player2 pieces for even rows
                    self.playerPieces[1][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='O{0:02d}'.format(pieceCounter), pieceLocation=(7-i, j))
                    self.spaces[7-i][j].setSpaceOwner(self.playerPieces[1][pieceCounter])
                else:
                    # initialize player1 pieces for odd rows
                    self.playerPieces[0][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='X{0:02d}'.format(pieceCounter), pieceLocation=(i, j))
                    self.spaces[i][j].setSpaceOwner(self.playerPieces[0][pieceCounter])
                    # initialize player2 pieces for odd rows
                    self.playerPieces[1][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='O{0:02d}'.format(pieceCounter), pieceLocation=(7-i, j+1))
                    self.spaces[7-i][j+1].setSpaceOwner(self.playerPieces[1][pieceCounter])
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

    def isValidMove(self, piece, player, currentLocation, moveType):
        vertical, horizontal = self.moveOptions[self._observers.index(player)][moveType]
        if ((currentLocation[0]+vertical > self.numRows) or (currentLocation[0]+vertical < 0)):
            return False
        elif ((currentLocation[1]+horizontal > self.numCols) or (currentLocation[1]+horizontal < 0)):
            return False
        else:
            if (moveType == 'jumpLeft' or moveType == 'jumpRight'):
                jumpedSpace = self.getSpaceByLocation(int(currentLocation[0]+vertical/2),  int(currentLocation[1]+horizontal/2))
                if ((jumpedSpace.getSpaceOwner() != player) and (jumpedSpace.getSpaceOwner() is not None)):
                    return True
            else:
                return True
        return False

    def movePlayerPiece(self, piece, player, moveType):
        currentLocation = piece.getLocation()
        vertical, horizontal = self.moveOptions[self._observers.index(player)][moveType]
        if self.isValidMove(piece, player, currentLocation, moveType):
            if (moveType == 'jumpLeft' or moveType == 'jumpRight'):
                # remove opponent piece, move piece
                jumpedSpace = self.getSpaceByLocation(int(currentLocation[0]+vertical/2),  int(currentLocation[1]+horizontal/2))
                if (jumpedSpace.getSpaceOwner() != player):
                    jumpedSpace.removeSpaceOwner()
                    #TODO: delete actual piece

            self.getSpaceByLocation(currentLocation[0], currentLocation[1]).removeSpaceOwner()
            self.getSpaceByLocation(currentLocation[0]+vertical, currentLocation[1]+horizontal).setSpaceOwner(piece)
            currentLocation = (currentLocation[0]+vertical, currentLocation[1]+horizontal)
        else:
            print('invalid move')
        return currentLocation

    #for testing
    def printBoard(self):
        for row in self.spaces:
            print(['---' if (space.getSpaceOwner() is None) else space.getSpaceOwner()._owner for space in row])
