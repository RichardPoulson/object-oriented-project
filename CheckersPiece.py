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

    def isValidMove(self, gameBoard, player, vertical, horizontal):
        # TODO: Check bounds on gameBoard, check if space is occupied
        return True

    def movePiece(self, gameBoard, player, moveType):
        vertical, horizontal = gameBoard.moveOptions[gameBoard._observers.index(player)][moveType]
        if self.isValidMove(gameBoard, player, vertical, horizontal):
            if (moveType == 'jumpLeft' or moveType == 'jumpRight'):
                # remove opponent piece, move piece
                jumpee = gameBoard.getSpaceByLocation(int(self.getLocation()[0]+vertical/2),  int(self.getLocation()[1]+horizontal/2))
                if (jumpee.getSpaceOwner() != player):
                    jumpee.removeSpaceOwner()
                    #TODO: delete actual piece

            gameBoard.getSpaceByLocation(self.getLocation()[0], self.getLocation()[1]).removeSpaceOwner()
            gameBoard.getSpaceByLocation(self.getLocation()[0]+vertical, self.getLocation()[1]+horizontal).setSpaceOwner(self)
            self.setLocation((self.getLocation()[0]+vertical, self.getLocation()[1]+horizontal))

        else:
            print('invalid move')
