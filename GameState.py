#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines GameState, which defines the state of a checkers game.
"""

"""
    for AIplayer, on update(), possibly get newGameBoard, then gamestate.set()
"""
from copy import deepcopy

class GameState:
  # Constructor
  def __init__(self, spaces, currentPlayer, lastMove):
    self.spaces = deepcopy(spaces) # copy objects instead of references
    self.currentPlayer = currentPlayer
    self.lastMove = deepcopy(lastMove)
  def setCurrentPlayer(self, currentPlayer): self.currentPlayer = currentPlayer
  def getCurrentPlayer(self): return self.currentPlayer
  def setSpaces(self, spaces): self.spaces = deepcopy(spaces)
  def getSpaces(self): return self.spaces
  def setLastMove(self, lastMove): self.lastMove = deepcopy(lastMove)
  def getLastMove(self): return self.lastMove
  def __iter__(self):
    return iter(self.spaces)