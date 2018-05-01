#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Richard Poulson
Defines the AlphaBetaSearch (ABS) class.  ABS is also passed a GameHeuristic, which assigns values to
GameStates according to the algorithm within that GameHeuristic.  What ABS's
"search(GameState, Int)" method does is analyze possible GameStates and return
a game "move" that is the most beneficial to the player specified in the GameHeuristic.  The second argument
for the search() method determines how many moves ahead the algorithm will
analyze.  By changing the number of moves that the algorithm will look ahead,
the difficulty of the AI player can be increased or decreased.

search() uses the minimax algorithm to traverse a GameState tree, with the
value of each tree node set by the GameHeuristic.  search() also uses alpha-beta
pruning to avoid analyzing branches of the tree that are unlikely (e.g. a player
choosing to put themselves in a bad situation).

@info:
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
http://www.flyingmachinestudios.com/programming/minimax/
"""

from sys import maxsize # used to set bounds of node values
from copy import copy, deepcopy # shallow or deep copy
from AlphaBetaNode import AlphaBetaNode as Node
from aiDecision import aiDecision

#== implement the aiDecision interface, can search
class AlphaBetaSearch(aiDecision): # returns an Action
    def __init__(self, checkers_board, game_heuristic):
        self.heuristic = game_heuristic # get passed the game heuristic that we will be using
    def search(self, board, max_num_moves):
        initial_node = Node(None, board) # initialize the first node with the given state of a board as its value
        # use the maxValue method to get the highest value possible from the given board's state
        highest_value = self.maxValue(initial_node, -maxsize - 1, maxsize, 0, max_num_moves)
        # retrieve node containing game move using the highest value as the key.  If more than one node has the
        #   same value as the highest value, will choose depending on the definition of node's iterator
        recommended_move_node = initial_node[highest_value]
        # retrieve the move from the node
        recommended_move = recommended_move_node.getMove()
        # retrieve the location (defined move[0]) from the move
        location_of_piece = recommended_move[0].getLocation()
        # pass the location to the board's method to receive the space relating to the location
        space_of_piece = board.getSpaceByLocation(location_of_piece[0], location_of_piece[1])
        # call the Piece's method to receive the actual Piece relating to the recommended move
        actual_piece = space_of_piece.getSpaceResident()
        # return (Piece, String)
        return (actual_piece, recommended_move[1]) # get child node value that matches key
    #== return the highest calculated utility value based on a given node and values
    def maxValue(self, node, alpha, beta, num_moves, max_num_moves):
        self.loadPossibleMoves(node) # use behavior to calculate all possible moves for the Player
        if ((num_moves == max_num_moves) or (node.hasChildren() == 0)): # maximum moves or no possible moves?
            # then pass node (and the game state inside it) to the game heuristic, receive the corresponding
            #   utility value of that game state
            return_value = self.heuristic.getUtilityValue(node.getValue())
            node.setKey(return_value) # key of node = utility value
            return return_value
        value = -maxsize-1    # assign lowest possible value
        current_alpha = copy(alpha) # make a local copy of the Alpha value to be modified inside the loop 
        for eachChild in node:
            # calculate the utility values of all the possible game states that might occur.  Opponent will
            #   likely choose a game state with the lowest possible utility value, so pick the highest value
            #   among them. 
            value = max(value, self.minValue(eachChild, current_alpha, beta, num_moves + 1, max_num_moves))
            if (value >= beta): # if this calculate utility value is higher than given Beta value:
                return value
            current_alpha = max(current_alpha, value) # update current value of local Alpha copy
        # after calculating the utility values of all possible game states, set the given node's key to the
        # maximum utility value
        node.setKey(value)
        # return the max value so that it's value can be used to recommend a move
        return value
    #== return the lowest calculated utility value based on a given node and passed values
    # algorithm nearly the same as maxValue, see comments above
    def minValue(self, node, alpha, beta, num_moves, max_num_moves):
        self.loadPossibleMoves(node)
        if ((num_moves == max_num_moves) or (node.hasChildren() == 0)):
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
    #== initialize nodes with the values of all possible game states, and insert then into the given node as children.
    def loadPossibleMoves(self, node):
        computer_player = self.heuristic.getComputerPlayer() # get the Computer Player
        # get all possible moves, only consider spacing between pieces, not the owners of the Pieces
        available_moves = node.getValue().getAvailableMoves()
        for piece, moveType in available_moves: # for each possible move:
            if( ((node.isMaxNode() == True) and (piece.getOwner().id == computer_player.id)) or # if Computer's turn and Computer's Piece
                ((node.isMaxNode() == False) and (piece.getOwner().id != computer_player.id))): # if Player's turn and Player's Piece
                playerID = piece.getOwner().id # get its ID
                location = piece.getLocation() # get its location
                potential_board = node.getValue().clone() # make a cloned instance of the game board
                for player in potential_board.observers: # for each player:
                    if ((player.id) == playerID): # if the player's ID matches the one above:
                        # get a pointer to that piece
                        moving_piece = potential_board.spaces[location[0]][location[1]].getSpaceResident()
                        # move that piece on the clone'd board according to the given player, location, and moveType
                        potential_board.movePlayerPiece(moving_piece, player, location, moveType)
                        # Initialize a new node with this altered game board as its value.  Also, set whether the node
                        # is a max node or not (opposite of given node) 
                        new_node = Node(node, potential_board, not(node.maxNode))
                        # set the attribute of the node, so that it knows what move resulted in its game state
                        new_node.setMove((copy(moving_piece), moveType))
                        # finally, add this node as a child of the given node.
                        node.addChild(new_node)