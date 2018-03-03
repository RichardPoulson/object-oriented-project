class Piece:

    def __init__(self, color=None, owner=None, isKing=False, location=None):
        self.setColor(color)
        self.setOwner(owner)
        self._isKing=False
        self.setLocation(location)

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
        pass
