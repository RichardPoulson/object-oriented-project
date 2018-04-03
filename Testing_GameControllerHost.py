from GameController import *

newGame = GameController()
player1 = HumanPlayer('1')
newGame.hostGame(player1)
#newGame.runGame()

player1.commSocket.sendMessage(input("Message 1: "))
player1.commSocket.receiveMessage()
