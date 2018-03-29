#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines an encapsulated "game state".  Will be used in the AlphaBetaSearch
algorithm.

https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
"""
from copy import deepcopy

class GameState:
  # Constructor
  def __init__(self, game_board, humans_turn, last_move = None):
    self.value = None # refers to a utility value for AI player.
    self.game_board = game_board
    self.humans_turn = humans_turn
    self.last_move = last_move # action/move that led to this game state
    self.spaces = deepcopy(self.game_board.spaces)
    self.possible_moves = [] # possible moves that can be made
  # allow GameState to be iterated through, elements are possible moves
  def __iter__(self):
    return iter(self.possible_moves)
  # used to determine if this MinMaxNode is == to another
  def __eq__(self, other):
    return (self.value == other.value)
  # used to determine if this MinMaxNode is < another
  def __lt__(self, other):
    return (self.value < other.value)
  def __getitem__(self, key):
    for child in self:
      if child.getValue() == key:
        return child

  def getAvailableMoves(self):
      pass
