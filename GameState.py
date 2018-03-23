#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines an encapsulated "game state".  Will be used in the AlphaBetaSearch
algorithm.

https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
"""

"""
    for AIplayer, on update(), possibly get newGameBoard, then gamestate.set()
"""
from copy import deepcopy

class GameState:
  # Constructor
  def __init__(self, current_player, last_move, game_board):
    self.value_ = None # refers to a utility value for AI player.
    self.current_player_ = current_player
    self.last_move_ = last_move
    self.game_board = game_board
    self.spaces = deepcopy(self.game_board.spaces)
    self.possible_moves = [] # possible moves that can be made
  # allow GameState to be iterated through, elements are possible moves
  def getValue(self):
    return self.value_
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
