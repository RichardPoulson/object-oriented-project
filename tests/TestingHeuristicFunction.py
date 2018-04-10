'''
Script of commands for testing the GameHeuristic interface and
the CheckersHeuristic class.  Will place Player's pieces in
different layouts, and call the CheckersHeuristic getUtility
function
'''

import sys
sys.path.append('../')

from GameController import *
from User import *
from CheckersHeuristic import CheckersHeuristic

newGame = GameController()
newGame.setGame(CheckersBoard())
player1 = HumanPlayer(1)
player2 = HumanPlayer(2)
heuristicFunction = CheckersHeuristic(newGame.game, player1)
newGame.game.initializeGameBoard(player1, player2)
newGame.game.printBoard()
for i in range(5):
  for player in newGame.game.observers:
    pieceID, moveType = newGame.view.getPlayerMove()
    player.makeMove(newGame.game, pieceID, moveType)
print(heuristicFunction.getUtilityValue(newGame.game))