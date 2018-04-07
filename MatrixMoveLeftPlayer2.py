from interface import implements
from MoveStrategy import *

class MatrixMoveLeftPlayer2(implements(MoveStrategy)):
    def locationChange(self):
        return (-1, -1)
