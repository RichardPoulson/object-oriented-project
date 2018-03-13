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
        i = 0
        while(i < 2):
            for player in self.game._observers:
                #fromSpaceRow = int(input("Piece Row:"))
                #fromSpaceCol = int(input("Piece Column:"))
                #pieceID = self.game.spaces[fromSpaceRow][fromSpaceCol].getSpaceOwner()
                pieceID = input("Piece ID: ")
                moveType = input("Move Type: ")
                player.makeMove(self.game, pieceID, moveType)
                #player.makeMove(self.game, self.game.playerPieces[1][9], 'moveLeft')
            i+=1



newGame = GameController()
player1 = HumanPlayer('1')
player2 = HumanPlayer('2')
newGame.hostGame(player1)
newGame.joinGame(player2)
newGame.runGame()
