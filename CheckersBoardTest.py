from CheckersBoard import *

board = CheckersBoard()
board.initializeGameBoard()
board.printBoard()
p = board.player1Pieces[8]
#p.movePiece(board, 3, 2)
board.makePlayer1Move(p, 2, 1, 'moveRight')
print()
board.printBoard()
