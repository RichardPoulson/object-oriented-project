from GameController import *
from User import *

newGame = GameController()
#player2 = HumanPlayer('2')
player2 = User()
newGame.joinGame(player2, socket.gethostbyname(''), 10000)
