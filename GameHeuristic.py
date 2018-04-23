# -*- coding: utf-8 -*-
"""
Interface for a game heuristic.  This interface is implemented by game
heuristics that assign a utility value to a given state of a game.

https://docs.python.org/3/library/abc.html
"""
from abc import ABCMeta, abstractmethod

class GameHeuristic(metaclass=ABCMeta):
  @abstractmethod
  def getUtilityValue(self, checkers_board):
    pass
