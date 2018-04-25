#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Richard Poulson
Defines the AlphaBetaSearch (ABS) class.  ABS is given a CheckersBoard and
makes a deep copy of it, so that it can work with the board without disrupting
the game.  ABS is also given a GameHeuristic, which assigns a values to
GameStates according to the algorithm within GameHeuristic.  What ABS's
"search(GameState, Int)" method does is analyze possible GameStates and return
a game "move" that is the most beneficial to the AI player.  The second argument
for the search() method determines how many moves ahead the algorithm will
analyze.  By changing the number of moves that the algorithm will look ahead,
the difficulty of the AI player can be increased or decreased.

search() uses the minimax algorithm to traverse a GameState tree, with the
value of each tree node set by the GameHeuristic.  search() also uses alpha-beta
pruning to avoid analyzing branches of the tree that are unlikely (e.g. a player
choosing to put themselves in a bad situation).

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
http://www.flyingmachinestudios.com/programming/minimax/
"""

from sys import maxsize # used to set bounds of node values
from copy import deepcopy # shallow or deep copy
from AlphaBetaNode import AlphaBetaNode as Node

class AlphaBetaSeach: # returns an Action
    def __init__(self, checkers_board, game_heuristic):
        # reference for calling CheckersBoard methods
        self.board = deepcopy(checkers_board)
        # responsible for assigning a heuristic value to GameStates
        self.heuristic = game_heuristic
    def search(self, state, max_num_moves):
        initial_num_moves = 0
        # Find the move that will result in the highest value (be the most
        # beneficial to the AI player)
        highest_value = self.maxValue(self.board, initial_num_moves, max_num_moves)
        return highest_value # get child node value that matches key
    def maxValue(self, checkers_board, moves_so_far, max_num_moves):
        if (moves_so_far == max_num_moves):
            # get utility value for this state
            return self.gameHeuristic.getUtilityValue(checkers_board)
        current_value = -maxsize - 1 # lowest possible value
        available_moves = checkers_board.getAvailableMoves()
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
