class Space:
    def __init__(self, locationI=None, locationJ=None):
        self.isOccupied = False
        self.spaceResident = None

    def getOccupancy(self):
        return self.isOccupied

    def setOccupancy(self, occupied):
        self.isOccupied = occupied

    def getSpaceResident(self):
        return self.spaceResident

    def setSpaceResident(self, resident):
        self.spaceResident = resident
        self.setOccupancy(True)

    def removeSpaceResident(self):
        self.spaceResident = None
        self.setOccupancy(False)
