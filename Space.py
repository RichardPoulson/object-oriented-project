class Space:
    def __init__(self):
        self._isOccupied = False
        self._location = None
        self._spaceOwner = None
        # for Testing
        self.icon = '-'

    def spaceOccupied(self):
        return self._isOccupied

    def getSpaceOwner(self):
        return self._spaceOwner

    def setSpaceOwner(self, owner):
        self._spaceOwner = owner

    def getLocation(self):
        return self._location

    def setLocation(self, newLocation):
        self._location = newLocation
