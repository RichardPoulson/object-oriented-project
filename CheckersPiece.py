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

    def movePiece(self, space):
        newSpaceOwner = newSpace.getOwner()
        if newSpaceOwner is None:
            self.setLocation(newSpace)
            newSpace.setOwner(self.getOwner())
        elif newSpaceOwner != self.getOwner():
            # jump over players piece, remove piece at that location
            return
        #else player already has one of their pieces on that space
        else:
            return
