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
# and the computer player (so that heuristic can tell which pieces are theirs)
heuristicFunction = CheckersHeuristic(newGame.game, computer_player)
newGame.game.addObserver(player1)
newGame.game.addObserver(computer_player)
# add some pieces to the board
addPiece('X00', player1, (0, 0), newGame.game)
addPiece('X01', player1, (3, 3), newGame.game)
addPiece('O00', computer_player, (4, 4), newGame.game)
addPiece('O01', computer_player, (7, 7), newGame.game)
# print the board
newGame.game.printBoard()
abs = AlphaBetaSearch(newGame.game, heuristicFunction)
recommended_move = abs.search(newGame.game, 2)
# abs.search() actually returns (Piece, String), however it's easier to display
# the Piece's location for the example
print(recommended_move[0].location, recommended_move[1])