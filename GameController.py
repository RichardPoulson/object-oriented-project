from CheckersBoard import *
from HumanPlayer import *
from Server import *
from ClientSocket import *
#from GameState import *

import time

class GameController:
    def __init__(self):
        self.game = None
        self.server = None

    def setGame(self, newGame):
        self.game = newGame

    def hostGame(self, humanPlayer):
        self.server = Server(socket.gethostbyname(''), 10000, CheckersBoard())
        self.setGame(self.server.game)
        self.server.run()
        humanPlayer.commSocket = ClientSocket(socket.gethostbyname(''), 10000, 1)
        #humanPlayer.addSelfToRemoteGame()

    def joinGame(self, humanPlayer):
        humanPlayer.commSocket = ClientSocket(socket.gethostbyname(''), 10000, 2)
        #humanPlayer.addSelfToRemoteGame()

    def runRemoteGame(self):
        self.server.game.initializeGameBoard()
        self.server.game.printBoard()

    def playAI(self, player):
        self.setGame(CheckersBoard())
        self.game.addObserver(player)
        pass

    def runLocalGame(self):
        self.game.initializeGameBoard()
        self.game.printBoard()

        gs = GameState(None, None, self.game)
        gs.getAvailableMoves()

        while(max(self.game.observers[0].getNumPieces(), self.game.observers[1].getNumPieces()) > 0):
            for player in self.game.observers:
                pieceID = input("Piece ID: ")
                moveType = input("Move Type: ")
                player.makeMove(self.game, pieceID, moveType)
