from CheckersBoard import *

board = CheckersBoard()
board.initializeGameBoard()
board.printBoard()
p = board.player1Pieces[8]
p.movePiece(board, 3, 2)
print()
board.printBoard()
