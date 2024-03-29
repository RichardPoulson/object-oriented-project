from GameObservable import *
from CheckersPiece import *
from Space import *
from MoveStrategyFactory import *
import numpy as np
from copy import copy, deepcopy

class CheckersBoard(GameObservable):

    def __init__(self):
        self.observers = []
        self.winner = None
        self.maxRows = 7
        self.maxCols = 7
        self.spaces = [[Space(locationJ=j, locationI=i) for i in range(0, self.maxCols+1)] for j in range(0, self.maxRows+1)]
        self.moveStrategyFactory = MoveStrategyFactory('matrix')
        self.moveStrategy = None

    def getWinner(self):
        return self.winner

    def setWinner(self):
        if (self.observers[0].getNumPieces() <= 0):
            self.winner = self.observers[1]
        elif (self.observers[1].getNumPieces() <= 0):
            self.winner = self.observers[0]
        else:
            self.winner = None

    def getMoveStrategy(self):
        return self.moveStrategy

    def setMoveStrategy(self, strategy):
        self.moveStrategy = strategy

    def initializeGameBoard(self, player1, player2):
        self.addObserver(player1)
        self.addObserver(player2)

        pieceCounter = 0
        for i in range(0, 3):
            for j in range(0, self.maxCols, 2):
                if ((i % 2) == 0):
                    # initialize player1 pieces for even rows
                    self.observers[0].addToPieceCollection('X{0:02d}'.format(pieceCounter), CheckersPiece(ID='X{0:02d}'.format(pieceCounter), owner=self.observers[0], location=(i, j+1)))
                    self.spaces[i][j+1].setSpaceResident(self.observers[0].getPieceFromCollection('X{0:02d}'.format(pieceCounter)))

                    # initialize player2 pieces for even rows
                    self.observers[1].addToPieceCollection('O{0:02d}'.format(pieceCounter), CheckersPiece(ID='O{0:02d}'.format(pieceCounter), owner=self.observers[1], location=(7-i, j)))
                    self.spaces[7-i][j].setSpaceResident(self.observers[1].getPieceFromCollection('O{0:02d}'.format(pieceCounter)))
                else:
                    # initialize player1 pieces for odd rows
                    self.observers[0].addToPieceCollection('X{0:02d}'.format(pieceCounter), CheckersPiece(ID='X{0:02d}'.format(pieceCounter), owner=self.observers[0], location=(i, j)))
                    self.spaces[i][j].setSpaceResident(self.observers[0].getPieceFromCollection('X{0:02d}'.format(pieceCounter)))
                    # initialize player2 pieces for odd rows
                    self.observers[1].addToPieceCollection('O{0:02d}'.format(pieceCounter), CheckersPiece(ID='O{0:02d}'.format(pieceCounter), owner=self.observers[1], location=(7-i, j+1)))
                    self.spaces[7-i][j+1].setSpaceResident(self.observers[1].getPieceFromCollection('O{0:02d}'.format(pieceCounter)))

                pieceCounter += 1

        for observer in self.observers:
            observer.setNumPieces()

        self.startTimer()

    def getState(self):
        pass

    def setState(self, newState):
        pass

    def getSpaceByLocation(self, rowIndex, columnIndex):
        returnSpace = None
        if (rowIndex >= 0 and columnIndex < len(self.spaces)) and (rowIndex >= 0 and columnIndex < len(self.spaces[0])):
            returnSpace = self.spaces[rowIndex][columnIndex]
        return returnSpace

    def isValidMove(self, player, currentLocation, moveType):
        self.setMoveStrategy(self.moveStrategyFactory.getMoveStrategy(player.id, moveType))
        vertical, horizontal = self.getMoveStrategy().locationChange()
        #vertical, horizontal = self.moveOptions[self.observers.index(player)][moveType]

        if ((currentLocation[0]+vertical > self.maxRows) or (currentLocation[0]+vertical < 0)):
            return False
        elif ((currentLocation[1]+horizontal > self.maxCols) or (currentLocation[1]+horizontal < 0)):
            return False
        elif (self.getSpaceByLocation(currentLocation[0]+vertical, currentLocation[1]+horizontal).getOccupancy()):
            return False

        else:
            if (moveType == 'moveRight' or moveType == 'moveLeft'):
                return True

            if (moveType == 'jumpLeft' or moveType == 'jumpRight'):
                jumpedSpace = self.getSpaceByLocation(int(currentLocation[0]+vertical/2),  int(currentLocation[1]+horizontal/2))
                # instructions below don't quite work right for cloned boards, had to make some modifications (use id), sorry!
                if (jumpedSpace.getSpaceResident() is not None) and (jumpedSpace.getSpaceResident().getOwner().id != player.id):
                #if (jumpedSpace.getSpaceResident() is not None) and (jumpedSpace.getSpaceResident().getOwner() != player):
                    return True
        return False

    def getAvailableMoves(self):
        availableMoves = []
        for player in self.observers:
            for piece in player.getPlayerPieces():
                for moveType in ['moveLeft', 'moveRight', 'jumpLeft', 'jumpRight']:
                    if self.isValidMove(player, piece.getLocation(), moveType):
                        availableMoves.append((piece, moveType))
        return availableMoves

    def movePlayerPiece(self, piece, player, currentLocation, moveType):
        self.setMoveStrategy(self.moveStrategyFactory.getMoveStrategy(player.id, moveType))
        vertical, horizontal = self.getMoveStrategy().locationChange()
        #vertical, horizontal = self.moveOptions[self.observers.index(player)][moveType]
        if self.isValidMove(player, currentLocation, moveType):
            if (moveType == 'jumpLeft' or moveType == 'jumpRight'):
                # remove opponent piece, move piece
                jumpedSpace = self.getSpaceByLocation(int(currentLocation[0]+vertical/2),  int(currentLocation[1]+horizontal/2))
                #TODO: decrement opponent player's piececount
                # instructions below don't quite work right for cloned boards, had to make some modifications (use id), sorry!
                # jumpedSpace.getSpaceResident().getOwner().decrementNumPieces()
                ownerID = jumpedSpace.getSpaceResident().getOwner().id
                for player in self.observers:
                    if(player.id == ownerID):
                        player.decrementNumPieces()
                jumpedSpace.removeSpaceResident()

            self.getSpaceByLocation(currentLocation[0], currentLocation[1]).removeSpaceResident()
            self.getSpaceByLocation(currentLocation[0]+vertical, currentLocation[1]+horizontal).setSpaceResident(piece)
            currentLocation = (currentLocation[0]+vertical, currentLocation[1]+horizontal)
        else:
            print('invalid move')

        self.notifyObservers()
        self.setWinner()

        return currentLocation

    def getCurrentGameState(self):
        return deepcopy(self)

    def getReadOnlyState(self):
        return ([['---' if (space.getSpaceResident() is None) else space.getSpaceResident().getID() for space in row] for row in self.spaces])

    #for testing
    def printBoard(self):
        for row in self.spaces:
            print(['---' if (space.getSpaceResident() is None) else space.getSpaceResident().ID for space in row])
        print()

    # make copies of observers/winner/spaces, references to others
    def clone(self):
        clone = CheckersBoard()
        clone.observers = deepcopy(self.observers)
        clone.winner = deepcopy(self.winner)
        clone.maxRows = self.maxRows
        clone.maxCols = self.maxCols
        clone.spaces = deepcopy(self.spaces)
        clone.moveStrategyFactory = self.moveStrategyFactory
        clone.moveStrategy = self.moveStrategy
        return clone
