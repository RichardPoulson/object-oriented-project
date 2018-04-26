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
from copy import copy, deepcopy # shallow or deep copy
from AlphaBetaNode import AlphaBetaNode as Node

class AlphaBetaSearch: # returns an Action
    def __init__(self, checkers_board, game_heuristic):
        self.heuristic = game_heuristic
    def search(self, board, max_num_moves):
        initial_node = Node(None, board)
        highest_value = self.maxValue(initial_node, -maxsize - 1, maxsize, 0, max_num_moves)
        recommended_move_node = initial_node[highest_value]
        recommended_move = recommended_move_node.getMove()
        location_of_piece = recommended_move[0].getLocation()
        space_of_piece = board.getSpaceByLocation(location_of_piece[0], location_of_piece[1])
        actual_piece = space_of_piece.getSpaceResident()
        return (actual_piece, recommended_move[1]) # get child node value that matches key
    def maxValue(self, node, alpha, beta, num_moves, max_num_moves):
        self.loadPossibleMoves(node)
        if ((num_moves == max_num_moves) or (node.hasChildren() == 0)):    # does this node not need to be evaluated?
            return_value = self.heuristic.getUtilityValue(node.getValue())
            node.setKey(return_value)
            return return_value
        value = -maxsize-1    # assign lowest possible value to val
        current_alpha = copy(alpha)
        for eachChild in node:
            value = max(value, self.minValue(eachChild, current_alpha, beta, num_moves + 1, max_num_moves))
            if (value >= beta):  # if this child's value is bigger than val..
                return value  # ..Min won't choose 
            current_alpha = max(current_alpha, value)
        node.setKey(value)
        return value
    def minValue(self, node, alpha, beta, num_moves, max_num_moves):
        self.loadPossibleMoves(node)
        if ((num_moves == max_num_moves) or (node.hasChildren() == 0)):    # does this node not need to be evaluated?
            return_value = self.heuristic.getUtilityValue(node.getValue())
            node.setKey(return_value)
            return return_value
        value = maxsize
        current_beta = copy(beta)
        for eachChild in node:
            value = min(value, self.maxValue(eachChild, alpha, current_beta, num_moves + 1, max_num_moves))
            if (value <= alpha):
                return value
            current_beta = min(current_beta, value)
        node.setKey(value)
        return value
    def loadPossibleMoves(self, node):
        computer_player = self.heuristic.getComputerPlayer()
        available_moves = node.getValue().getAvailableMoves()
        for piece, moveType in available_moves:
            if( ((node.isMaxNode() == True) and (piece.getOwner().id == computer_player.id)) or
                ((node.isMaxNode() == False) and (piece.getOwner().id != computer_player.id))):
                playerID = piece.getOwner().id
                location = piece.getLocation()
                potential_board = node.getValue().clone()
                for player in potential_board.observers:
                    if ((player.id) == playerID):
                        moving_piece = potential_board.spaces[location[0]][location[1]].getSpaceResident()
                        potential_board.movePlayerPiece(moving_piece, player, location, moveType)
                        new_node = Node(node, potential_board, not(node.maxNode))
                        new_node.setMove((copy(moving_piece), moveType))
                        node.addChild(new_node)