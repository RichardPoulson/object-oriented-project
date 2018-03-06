class Space:
    def __init__(self):
        self._isOccupied = False
        self._location = None
        self._spaceOwner = None
        # for Testing
        self.icon = '-'

    def spaceOccupied(self):
        return this._isOccupied

    def getSpaceOwner(self):
        return this._spaceOwner

    def setSpaceOwner(self, owner):
        this._spaceOwner = owner

    def getLocation(self):
        return this._location

    def setLocation(self, newLocation):
        this._location = newLocation
