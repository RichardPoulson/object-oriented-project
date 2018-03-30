# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/abc.html
"""
from abc import ABCMeta, abstractmethod

class GameHeuristic(metaclass=ABCMeta):
  @abstractmethod
  def getUtilityValue(self, GameState):
    pass
