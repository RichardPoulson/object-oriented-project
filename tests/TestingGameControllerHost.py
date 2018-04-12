import sys
sys.path.append('../')

from GameController import *
from User import *

newGame = GameController()
player1 = User()
newGame.hostGame(player1, socket.gethostbyname(''), 10000)
