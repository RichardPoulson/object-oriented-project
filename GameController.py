from CheckersBoard import *
from HumanPlayer import *

class GameController:
    def __init__(self):
        self.game = None

    def setGame(self, newGame):
        self.game = newGame

    def hostGame(self, player):
        self.setGame(CheckersBoard())
        self.game.addObserver(player)

    def joinGame(self, player):
        self.game.addObserver(player)

    def runGame(self):
        self.game.initializeGameBoard()
        self.game.printBoard()
        while(max(self.game.observers[0].getNumPieces(), self.game.observers[1].getNumPieces()) > 0):
            for player in self.game.observers:
                pieceID = input("Piece ID: ")
                moveType = input("Move Type: ")
                player.makeMove(self.game, pieceID, moveType)


newGame = GameController()
player1 = HumanPlayer('1')
player2 = HumanPlayer('2')
newGame.hostGame(player1)
newGame.joinGame(player2)
newGame.runGame()
