from interface import implements
from Piece import *

class CheckersPiece(implements(Piece)):

    def __init__(self, ID=None, owner=None, isKing=False, location=None):
        self._ID = ID
        self._owner = owner
        # may be a good idea to make King a separate class
        self._isKing = isKing
        self._location = location

    def getID(self):
        return self._ID

    def setID(self, ID):
        self._ID = ID

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

    def movePiece(self, gameBoard, player, moveType):
        self.setLocation(gameBoard.movePlayerPiece(self, player, self.getLocation(), moveType))
