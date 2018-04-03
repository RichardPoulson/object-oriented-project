from GameController import *

newGame = GameController()
player2 = HumanPlayer('2')
newGame.joinGame(player2)
#newGame.runGame()

newState = player2.commSocket.fetchState()
for row in newState:
    print(row)
