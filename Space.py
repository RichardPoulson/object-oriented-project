class Space:
    def __init__(self, locationI=None, locationJ=None):
        self._isOccupied = False
        # TODO: these should not be hardcoded as matrix indices
        self._locationI = locationI
        self._locationJ = locationJ
        self._spaceOwner = None

    def getOccupancy(self):
        return self._isOccupied

    def setOccupancy(self, occupied):
        self._isOccupied = occupied

    def setUnoccupied(self):
        self._isOccupied = False
        self._spaceOwner = None

    def getSpaceOwner(self):
        return self._spaceOwner

    def setSpaceOwner(self, owner):
        self._spaceOwner = owner
        self.setOccupancy(True)

    def removeSpaceOwner(self):
        self._spaceOwner = None
        self.setOccupancy(False)

    def getLocation(self):
        # TODO: this should not be hardcoded as a matrix
        return (self._locationI, self.locationJ)

    def setLocation(self, newLocation):
        self._location = newLocation
