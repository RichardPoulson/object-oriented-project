#from MoveStrategy import *

class MoveStrategyFactory:
    def __init__(self, gameBoardDataStructure):
        self.dataStructure = gameBoardDataStructure

    def getMoveStrategy(self, moveType):
        if (self.dataStructure == 'matrix'):
            return self.getMatrixMoveStrategy(moveType)

    def getMatrixMoveStrategy(self, moveType):
        if (moveType == 'moveLeft'): return MatrixMoveLeft()
        elif (moveType == 'moveRight'): return MatrixMoveRight()
        elif (moveType == 'jumpLeft'): return MatrixJumpLeft()
        elif(moveType == 'jumpRight'): return MatrixJumpRight()

factory = MoveStrategyFactory('matrix')
factory.getMoveStrategy('moveRight')
