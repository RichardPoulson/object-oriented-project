from CheckersBoard import *
from HumanPlayer import *

board = CheckersBoard()
player1 = HumanPlayer('1')
player2 = HumanPlayer('2')
board.addObserver(player1)
board.addObserver(player2)
board.initializeGameBoard()
board.printBoard()
player1.makeMove(board, board.playerPieces[0][8], 'moveRight')
player2.makeMove(board, board.playerPieces[1][9], 'moveLeft')
print()
board.printBoard()
player1.makeMove(board, board.playerPieces[0][8], 'jumpLeft')
print()
board.printBoard()
