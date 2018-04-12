from interface import implements
from MoveStrategy import *

class MatrixJumpLeftPlayer2(implements(MoveStrategy)):
    def locationChange(self):
        return (-2, -2)
