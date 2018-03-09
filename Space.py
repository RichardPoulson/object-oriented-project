class Space:
    def __init__(self, locationY=None, locationX=None):
        self._isOccupied = False
        self._locationY = locationY
        self._locationX = locationX
        self._spaceOwner = None

    def getOccupancy(self):
        return self._isOccupied

    def setOccupied(self):
        self._isOccupied = True

    def setUnoccupied(self):
        self._isOccupied = False
        self._spaceOwner = None

    def getSpaceOwner(self):
        return self._spaceOwner

    def setSpaceOwner(self, owner):
        self._spaceOwner = owner
        self.setOccupied()

    def getLocation(self):
        return self._location

    def setLocation(self, newLocation):
        self._location = newLocation
