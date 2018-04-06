from GameController import *
from User import *

newGame = GameController()
#player1 = HumanPlayer('1')
player1 = User()
newGame.hostGame(player1, socket.gethostbyname(''), 10000)
#newGame.runRemoteGame()
