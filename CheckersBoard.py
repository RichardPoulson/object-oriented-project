from GameObservable, PieceFactory import *
#from Space import *

class CheckersBoard(GameObservable):
    player1Pieces = []
    player2Pieces = []

    #self.spaces = []

    def __init__(self):
        self.player1Pieces = [getPiece()]*10
        self.player2Pieces = [getPiece()]*10
        #self.spaces = [[Space()]*8]*8

    def getState(self):
        pass

    def setState(self):
        pass
