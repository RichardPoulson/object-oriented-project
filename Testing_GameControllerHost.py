from GameController import *
from User import *

newGame = GameController()
#player1 = HumanPlayer('1')
player1 = User()
newGame.hostGame(player1)
newGame.runRemoteGame()

newGame.game.getServer().sendState()
newState = player1.commSocket.fetchState()
for row in newState:
    print(row)

'''
time.sleep(5)
#newGame.server.sendState()
#newState = player1.commSocket.fetchState()
#for row in newState:
#    print(row)

player1.commSocket.sendMessage(input("Message 1: "))
player1.commSocket.receiveMessage()
'''
