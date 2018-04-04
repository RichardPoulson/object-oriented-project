from CheckersBoard import *
from RemoteCheckersBoard import *
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

    def hostGame(self, user):
        self.setGame(RemoteCheckersBoard(Server(socket.gethostbyname(''), 10000)))
        self.game.getServer().run()
        user.commSocket = ClientSocket(socket.gethostbyname(''), 10000, 1)
        while (self.game.getServer().getNumberOfClientConnections() < 2):
            print("waiting for user to join...")
            time.sleep(2)
        #humanPlayer.addSelfToRemoteGame()

    def joinGame(self, user):
        user.commSocket = ClientSocket(socket.gethostbyname(''), 10000, 2)
        #humanPlayer.addSelfToRemoteGame()

    def runRemoteGame(self):
        self.game.addObserver(HumanPlayer('1'))
        self.game.addObserver(HumanPlayer('2'))
        self.game.initializeGameBoard()
        #self.server.game.printBoard()

    def playAI(self, humanPlayer):
        #self.setGame(CheckersBoard())
        #self.game.addObserver(humanPlayer)
        #self.game.addObserver(AIPlayer())
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
