import sys
sys.path.append('../')

from GameController import *
from User import *

newGame = GameController()
newGame.startApplication()
newGame.setGame(CheckersBoard())
newGame.runLocalGame()
