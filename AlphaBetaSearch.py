#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Richard Poulson
Defines the MinMaxNode class, methods for that class, and the
Alpha-Beta pruning algorithm for assigning values MinMaxNodes.

https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
"""

from sys import maxsize # maxsize used to compare other node values
# from copy import copy # to make copies of alpha and beta

class AlphaBetaSeach:
  # at this point, the class has no attributes
  def __init__(self):
    pass
  def search(self, state, max_num_moves):
    # hasn't made any moves yet, so set to 0
    initial_num_moves = 0
    # Find the action that will lead to the state with the highest possible
    # value.
    highest_value = self.maxValue(state, -maxsize-1, maxsize, initial_num_moves, max_num_moves)
    return state[highest_value]
  def maxValue(self, state, alpha, beta, moves_so_far, max_num_moves):
    if (moves_so_far >= max_num_moves): # have we looked far enough ahead?
      return state.utilityValue() # if so, get the utility value for this state
    current_value = -maxsize - 1 # lowest possible value
    # current_alpha = copy(alpha) # make a copy so it doesn't reference original
    # current_num_moves = copy(moves_so_far) # ""
    for following_state in state: # for every possible action/move in this state:
      # find the move with the lowest value, since this would be the opposing
      # player's best move
      temp_value = self.minValue(following_state, alpha, beta, moves_so_far, max_num_moves)
      # out of all the possible states made by the opposing player's moves,
      # choose the one with the highest value, since this would benefit the
      # computer player
      current_value = max(current_value, temp_value)
      # if condition true, opposing player probably won't choose a move on this
      # branch, so simply return the current value without checking any other
      # game states
      if (current_value >= beta):
        return current_value
      # set the current upper-bound value for this game state
      alpha = max(alpha, current_value)
    # found the value for the game state, so set state value and return value
    state.setValue(current_value)
    return current_value
  def minValue(self, state, alpha, beta, moves_so_far, max_num_moves):
    if (moves_so_far >= max_num_moves): # have we looked far enough ahead?
      return state.utilityValue() # if so, get the utility value for this state
    current_value = maxsize # maximum size possible
    # current_beta = copy(beta)
    for following_state in state:
      temp_value = self.maxValue(following_state, alpha, beta, moves_so_far, max_num_moves)
      current_value = min(current_value, temp_value)
      # if condition true, don't want to choose this path, since it will most
      # likely end up with a very low utility value.  Simply return value
      # without checking any more states
      if (current_value <= alpha):
        return current_value
      # set beta to the lowest value found so fare
      beta = min(beta, current_value)
    state.setValue(current_value)
    return current_value