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
        self.setGame(CheckersBoard())
        self.server = Server(socket.gethostbyname(''), 10000, self.game)
        self.server.run()
        humanPlayer.commSocket = ClientSocket(socket.gethostbyname(''), 10000, 1)
        #self.game.addObserver(player)

    def joinGame(self, humanPlayer):
        humanPlayer.commSocket = ClientSocket(socket.gethostbyname(''), 10000, 2)
        time.sleep(1)
        #self.game.addObserver(player)

    def playAI(self, player):
        self.setGame(CheckersBoard())
        self.game.addObserver(player)
        pass

    def runGame(self):
        self.game.initializeGameBoard()
        self.game.printBoard()

        gs = GameState(None, None, self.game)
        gs.getAvailableMoves()

        while(max(self.game.observers[0].getNumPieces(), self.game.observers[1].getNumPieces()) > 0):
            for player in self.game.observers:
                pieceID = input("Piece ID: ")
                moveType = input("Move Type: ")
                player.makeMove(self.game, pieceID, moveType)

'''
newGame = GameController()
player1 = HumanPlayer('1')
player2 = HumanPlayer('2')
newGame.hostGame(player1)
newGame.joinGame(player2)
#newGame.runGame()

player1.commSocket.sendMessage(input("Message 1: "))
player1.commSocket.receiveMessage()
player2.commSocket.receiveMessage()
player2.commSocket.sendMessage(input("Message 2: "))
player1.commSocket.receiveMessage()
player2.commSocket.receiveMessage()
'''
