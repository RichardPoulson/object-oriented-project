# -*- coding: utf-8 -*-
"""
This class implements GameHeuristic and is responsible for
assigning a utility value to the current state of a given
checkers board.
"""
from GameHeuristic import GameHeuristic

class CheckersHeuristic(GameHeuristic):
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
  def getUtilityValue(self, checkers_board):
    utilityValue = 0
    for eachPlayer in checkers_board.observers:
      if (eachPlayer == self.computerPlayer):
        utilityValue += eachPlayer.getNumPieces()
      else:
        utilityValue -= eachPlayer.getNumPieces()
    return utilityValue