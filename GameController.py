from CheckersBoard import *
from HumanPlayer import *
from GameServer import *

class GameController:
    def __init__(self):
        #self.game = None
        self.server = None

    def setGame(self, newGame):
        self.game = newGame

    def getServer(self):
        return self.server

    def setServer(self, newServer):
        self.server = newServer

    def hostGame(self, player, address, port):
        self.setServer(GameServer(address, port, CheckersBoard()))
        self.getServer().addConnection(player)

    def joinGame(self, player):
        self.getServer().addConnection(player)

    def runGame(self):
        self.game.initializeGameBoard()
        self.game.printBoard()
        while(max(self.game._observers[0].getNumPieces(), self.game._observers[1].getNumPieces()) > 0):
            for player in self.game._observers:
                pieceID = input("Piece ID: ")
                moveType = input("Move Type: ")
                player.makeMove(self.game, pieceID, moveType)


newGame = GameController()
player1 = HumanPlayer('1')
player2 = HumanPlayer('2')
newGame.hostGame(player1, socket.gethostbyname(''), 1235)
newGame.joinGame(player2)
player1.setObservingGameState(newGame.server.getGameState())
player2.setObservingGameState(newGame.server.getGameState())
#newGame.runGame()

newGame.server.notify()

player1.playerSocket.close()
newGame.server.closeServer()
