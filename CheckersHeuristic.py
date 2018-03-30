# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/abc.html
"""
from HeuristicFunction import HeuristicFunction

class CheckersHeuristic(HeuristicFunction):
  def __init__(self, computerPlayer, initialGameState):
    self.computerPlayer = computerPlayer
    self.initialGameState = initialGameState
  def getUtilityValue(self, GameState):
    utilityValue = 0
    for eachSpace in GameState:
      if (eachSpace.getOccupancy()):
        current_piece = eachSpace.getSpaceResident()
        if (current_piece.getOwner() == self.computerPlayer):
          if(current_piece.isKing()):
            utilityValue +=2
          else:
            utilityValue += 1
        else:
          if(current_piece.isKing()):
            utilityValue -= 2
          else:
            utilityValue -= 1
    return utilityValue