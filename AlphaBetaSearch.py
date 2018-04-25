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
        self.heuristic = game_heuristic
    def search(self, board, max_num_moves):
        initial_node = Node(None, board)
        num_moves = 0
        highest_value = self.maxValue(initial_node, num_moves, max_num_moves)
        return highest_value # get child node value that matches key
    def maxValue(self, node, num_moves, max_num_moves):
        if (num_moves == max_num_moves):    # does this node not need to be evaluated?
            return self.heuristic.getUtilityValue(node.getValue()):
        temp_alpha = node.getAlpha()    # the current maximum to be searched against
        val = -maxsize-1    # assign lowest possible value to val
        # temporary values
        for eachChild in self.children:
            (tmpVal, tmpCount) = eachChild.minValue(tmpAlpha, beta)  # get the
            # value and evaluation count from eachChild
            val = max(val, tmpVal)  # update val to the new maximum value
            count += tmpCount  # add evaluation count of child to this count
            if (val >= beta):  # if this child's value is bigger than val..
                return (val, count)  # ..Min won't choose 
            tmpAlpha = max(tmpAlpha, val)
        self.val = val  
        return (val, count)
    def minValue(self, alpha, beta):
        if (self.val != None and self.children == None):
            return (self.val, 1)
        elif (self.val != None and self.children != None):
            return (self.val, 0)
        tmpBeta = beta
        val = maxsize
        for eachChild in self.children:
            (tmpVal, tmpCount) = eachChild.maxValue(alpha, tmpBeta)
            val = min(val, tmpVal)
            if (val <= alpha):
                return (val, count)
                tmpBeta = min(tmpBeta, val)
        self.val = val 
        return (val, count)
    def loadPossibleMoves(self, node):
        computer_player = self.heuristic.getComputerPlayer()
        available_moves = node.getValue().getAvailableMoves()
        for piece, move_type in available_moves:
            if piece.getOwner() == computer_player:
                print(move_type)