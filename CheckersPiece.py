from interface import implements
from Piece import *

class CheckersPiece(implements(Piece)):

    def __init__(self, color=None, owner=None, isKing=False, location=None):
        self._color = color
        self._owner = owner
        # may be a good idea to make King a separate class
        self._isKing = isKing
        self._location = location

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getOwner(self):
        return self._owner

    def setOwner(self, owner):
        self._owner = owner

    def isKing(self):
        return self._isKing

    def makeKing(self):
        self._isKing = True

    def getLocation(self):
        return self._location

    def setLocation(self, location):
        self._location = location

    def movePiece(self, gameBoard, newSpaceRow, newSpaceColumn):
        oldSpace = self.getLocation()
        newSpace = gameBoard.getSpaceByLocation(newSpaceRow, newSpaceColumn)
        if (newSpace.getOccupancy() == False):
            if ((abs(oldSpace._locationY - newSpaceRow) == 1) and (abs(oldSpace._locationX - newSpaceColumn) == 1)):
                oldSpace.setUnoccupied()
                newSpace.setSpaceOwner(self)
                self.setLocation(newSpace)
            elif ((abs(oldSpace._locationY - newSpaceRow) == 2) and (abs(oldSpace._locationX - newSpaceColumn) == 2)):
                pass


        #else illegal move
        else:
            return

    def jumpPiece(self, gameBoard, newSpaceRow, newSpaceColumn):
        oldSpace = self.getLocation()
        newSpace = gameBoard.getSpaceByLocation(newSpaceRow, newSpaceColumn)
        if (newSpace.getOccupancy() == False):
            if ((abs(oldSpace._locationY - newSpaceRow) == 2) and (abs(oldSpace._locationX - newSpaceColumn) == 2)):
                oldSpace.setUnoccupied()
                newSpace.setSpaceOwner(self)
                self.setLocation(newSpace)
        #else illegal move
        else:
            return
