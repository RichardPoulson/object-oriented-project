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
        return highest_value # get child node value that matches key
    def maxValue(self, node, alpha, beta, num_moves, max_num_moves):
        self.loadPossibleMoves(node)
        if ((num_moves == max_num_moves) or (node.hasChildren() == 0)):    # does this node not need to be evaluated?
            return_value = self.heuristic.getUtilityValue(node.getValue())
            if(return_value != 0):
                node.getValue().printBoard()
                print(return_value)
            return self.heuristic.getUtilityValue(node.getValue())
        value = -maxsize-1    # assign lowest possible value to val
        current_alpha = copy(alpha)
        for eachChild in node:
            value = max(value, self.minValue(eachChild, current_alpha, beta, num_moves + 1, max_num_moves))
            if (value >= beta):  # if this child's value is bigger than val..
                return value  # ..Min won't choose 
            current_alpha = max(current_alpha, value)
        return value
    def minValue(self, node, alpha, beta, num_moves, max_num_moves):
        self.loadPossibleMoves(node)
        if ((num_moves == max_num_moves) or (node.hasChildren() == 0)):    # does this node not need to be evaluated?
            return_value = self.heuristic.getUtilityValue(node.getValue())
            if(return_value != 0):
                node.getValue().printBoard()
                print(return_value)
            return self.heuristic.getUtilityValue(node.getValue())
        value = maxsize
        current_beta = copy(beta)
        for eachChild in node:
            value = min(value, self.maxValue(eachChild, alpha, current_beta, num_moves + 1, max_num_moves))
            if (value <= alpha):
                return value
            current_beta = min(current_beta, value)
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
                        node.addChild(Node(node, potential_board, not(node.maxNode)))  
    def movePlayerPiece(self, board, piece, player, currentLocation, moveType):
        board.setMoveStrategy(board.moveStrategyFactory.getMoveStrategy(player.id, moveType))
        vertical, horizontal = board.getMoveStrategy().locationChange()
        #vertical, horizontal = self.moveOptions[self.observers.index(player)][moveType]
        if board.isValidMove(player, currentLocation, moveType):
            if (moveType == 'jumpLeft' or moveType == 'jumpRight'):
                # remove opponent piece, move piece
                jumpedSpace = board.getSpaceByLocation(int(currentLocation[0]+vertical/2),  int(currentLocation[1]+horizontal/2))
                #TODO: decrement opponent player's piececount
                jumpedSpace.getSpaceResident().getOwner().decrementNumPieces()
                print("jumped!")
                jumpedSpace.removeSpaceResident()

            board.getSpaceByLocation(currentLocation[0], currentLocation[1]).removeSpaceResident()
            board.getSpaceByLocation(currentLocation[0]+vertical, currentLocation[1]+horizontal).setSpaceResident(piece)
            currentLocation = (currentLocation[0]+vertical, currentLocation[1]+horizontal)