from MoveStrategy import *
from MatrixMoveLeftPlayer1 import *
from MatrixMoveLeftPlayer2 import *
from MatrixMoveRightPlayer1 import *
from MatrixMoveRightPlayer2 import *
from MatrixJumpLeftPlayer1 import *
from MatrixJumpLeftPlayer2 import *
from MatrixJumpRightPlayer1 import *
from MatrixJumpRightPlayer2 import *

class MoveStrategyFactory:
    def __init__(self, gameBoardDataStructure):
        self.dataStructure = gameBoardDataStructure

    def getMoveStrategy(self, playerNumber, moveType):
        if (self.dataStructure == 'matrix'):
            return self.getMatrixMoveStrategy(playerNumber, moveType)

    def getMatrixMoveStrategy(self, playerNumber, moveType):
        if (playerNumber == 1):
            if (moveType == 'moveLeft'): return MatrixMoveLeftPlayer1()
            elif (moveType == 'moveRight'): return MatrixMoveRightPlayer1()
            elif (moveType == 'jumpLeft'): return MatrixJumpLeftPlayer1()
            elif(moveType == 'jumpRight'): return MatrixJumpRightPlayer1()

        elif (playerNumber == 2):
            if (moveType == 'moveLeft'): return MatrixMoveLeftPlayer2()
            elif (moveType == 'moveRight'): return MatrixMoveRightPlayer2()
            elif (moveType == 'jumpLeft'): return MatrixJumpLeftPlayer2()
            elif(moveType == 'jumpRight'): return MatrixJumpRightPlayer2()
