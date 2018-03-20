from interface import Interface, implements

class Player(Interface):
    def __init__(self):
        pass

    def update(self, gameState):
        pass

    def makeMove(self, gameBoard, pieceID, moveType):
        pass
