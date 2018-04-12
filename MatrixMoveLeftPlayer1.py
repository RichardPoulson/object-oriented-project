from interface import implements
from MoveStrategy import *

class MatrixMoveLeftPlayer1(implements(MoveStrategy)):
    def locationChange(self):
        return (1, 1)
