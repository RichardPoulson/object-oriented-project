'''
Script of commands for testing the GameHeuristic interface and
the CheckersHeuristic class.  Will place Player's pieces in
different layouts, and call the CheckersHeuristic getUtility
function
'''
import sys
sys.path.append('../')

from GameController import GameController
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
player2 = HumanPlayer(2)
newGame = GameController()
newGame.setGame(CheckersBoard())
# the arguments to create a CheckersHeuristic instance are a checkers board
#   and the computer player (so that heuristic can tell which pieces are theirs)
heuristicFunction = CheckersHeuristic(newGame.game, player1)
newGame.game.addObserver(player1)
newGame.game.addObserver(player2)
# add some pieces to the board
addPiece('X00', player1, (0, 0), newGame.game)
addPiece('X01', player1, (1, 1), newGame.game)
newGame.game.printBoard()
print("Utility value =", heuristicFunction.getUtilityValue(newGame.game))

available_moves = newGame.game.getAvailableMoves()
for piece, move_type in available_moves:
    if piece.getOwner() == player1:
        print(move_type)
