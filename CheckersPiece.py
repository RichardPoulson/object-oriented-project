from interface import implements
from Piece import *

class CheckersPiece(implements(Piece)):

    def __init__(self, ID=None, owner=None, isKing=False, location=None):
        self.ID = ID
        self.owner = owner
        # may be a good idea to make King a separate class
        self.isKing = isKing
        self.location = location

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getOwner(self):
        return self.owner

    def setOwner(self, owner):
        self.owner = owner

    def isKing(self):
        return self.isKing

    def makeKing(self):
        self.isKing = True

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def movePiece(self, gameBoard, player, moveType):
        self.setLocation(gameBoard.movePlayerPiece(self, player, self.getLocation(), moveType))
