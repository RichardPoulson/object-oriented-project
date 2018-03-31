# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/abc.html
"""
from HeuristicFunction import HeuristicFunction

class CheckersHeuristic(HeuristicFunction):
  def __init__(self, checkersBoard, computerPlayer):
    self.setCheckersBoard(checkersBoard)
    self.setComputerPlayer(computerPlayer)
  def setCheckersBoard(self, newCheckersBoard):
    self.checkersBoard = newCheckersBoard
  def getCheckersBoard(self):
    return self.checkersBoard
  def setComputerPlayer(self, newComputerPlayer):
    self.computerPlayer = newComputerPlayer
  def getComputerPlayer(self):
    return self.computerPlayer
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