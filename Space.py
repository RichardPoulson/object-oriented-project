class Space:
    def __init__(self, locationI=None, locationJ=None):
        self._isOccupied = False
        # TODO: these should not be hardcoded as matrix indices
        self._locationI = locationI
        self._locationJ = locationJ
        self._spaceResident = None

    def getOccupancy(self):
        return self._isOccupied

    def setOccupancy(self, occupied):
        self._isOccupied = occupied

    def setUnoccupied(self):
        self._isOccupied = False
        self._spaceResident = None

    def getSpaceResident(self):
        return self._spaceResident

    def setSpaceResident(self, owner):
        self._spaceResident = owner
        self.setOccupancy(True)

    def removeSpaceResident(self):
        self._spaceResident = None
        self.setOccupancy(False)

    def getLocation(self):
        # TODO: this should not be hardcoded as a matrix
        return (self._locationI, self.locationJ)

    def setLocation(self, newLocation):
        self._location = newLocation
