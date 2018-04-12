from interface import implements
from MoveStrategy import *

class MatrixMoveRightPlayer1(implements(MoveStrategy)):
    def locationChange(self):
        return (1, -1)
