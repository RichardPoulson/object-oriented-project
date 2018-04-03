from GameController import *

newGame = GameController()
player1 = HumanPlayer('1')
newGame.hostGame(player1)
#newGame.runRemoteGame()


time.sleep(5)
#newGame.server.sendState()
#newState = player1.commSocket.fetchState()
#for row in newState:
#    print(row)

player1.commSocket.sendMessage(input("Message 1: "))
player1.commSocket.receiveMessage()
