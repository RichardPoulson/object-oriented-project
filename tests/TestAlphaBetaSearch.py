'''
Script of commands for testing the GameHeuristic interface and
the CheckersHeuristic class.  Will place Player's pieces in
different layouts, and call the CheckersHeuristic getUtility
function
'''
import sys
sys.path.append('../')

from GameController import GameController
from AlphaBetaSearch import AlphaBetaSearch
from HumanPlayer import HumanPlayer
from CheckersBoard import CheckersBoard
from CheckersHeuristic import CheckersHeuristic
from CheckersPiece import CheckersPiece
from Piece import Piece

#===  HELPER METHODS  ======================================
def addPiece(pieceID, owner, location, checkersBoard):
    newPiece = CheckersPiece(pieceID, owner)
    newPiece.setLocation(location)
    owner.addToPieceCollection(pieceID, newPiece)
    checkersBoard.spaces[location[0]][location[1]].setSpaceResident(newPiece)
    owner.setNumPieces()

#===  SCRIPT  ==============================================
player1 = HumanPlayer(1)
computer_player = HumanPlayer(2)
newGame = GameController()
newGame.setGame(CheckersBoard())
# the arguments to create a CheckersHeuristic instance are a checkers board
#   and the computer player (so that heuristic can tell which pieces are theirs)
newGame.game.initializeGameBoard(player1, computer_player)
# add some pieces to the board

newGame.game.printBoard()
heuristicFunction = CheckersHeuristic(newGame.game, player1)
abs = AlphaBetaSearch(newGame.game, heuristicFunction)
print (abs.search(newGame.game, 6))
