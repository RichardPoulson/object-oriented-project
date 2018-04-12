import sys
sys.path.append('../')

from MoveStrategyFactory import *

factory = MoveStrategyFactory('matrix')

for playerNumber in [1, 2]:
    for moveType in ['moveLeft', 'moveRight', 'jumpLeft', 'jumpRight']:
        print("Player {} {}: {}".format(playerNumber, moveType, factory.getMoveStrategy(playerNumber, moveType).locationChange()))

'''
key:
player1:
{'moveLeft':(1,1), 'moveRight':(1,-1), 'jumpLeft':(2,2), 'jumpRight':(2,-2)}

player2L
{'moveLeft':(-1,-1), 'moveRight':(-1,1), 'jumpLeft':(-2,-2), 'jumpRight':(-2,2)}
'''
