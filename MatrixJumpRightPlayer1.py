from interface import implements
from MoveStrategy import *

class MatrixJumpRightPlayer1(implements(MoveStrategy)):
    def locationChange(self):
        return (2, -2)
