from GameController import *

newGame = GameController()
player2 = HumanPlayer('2')
newGame.joinGame(player2)
#newGame.runGame()

player2.commSocket.receiveMessage()
