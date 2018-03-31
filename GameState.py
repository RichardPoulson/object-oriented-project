#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines GameState, which defines the state of a checkers game.
"""

"""
    for AIplayer, on update(), possibly get newGameBoard, then gamestate.set()
"""
from copy import copy, deepcopy

class GameState:
  def __init__(self, checkersBoard, currentPlayer, lastMove):
    self.setCheckersBoard(checkersBoard)
    self.setSpaces(self.getCheckersBoard().spaces)
    self.setCurrentPlayer(currentPlayer)
    self.setLastMove(lastMove)
    self.possibleMoves = []
  def setCheckersBoard(self, newCheckersBoard):
    self.checkersBoard = newCheckersBoard
  def getCheckersBoard(self, newCheckersBoard):
    self.checkersBoard = newCheckersBoard
  def setSpaces(self, spaces):
    self.spaces = copy(spaces) # copies object instead of reference
  def getSpaces(self):
    return self.spaces
  def setCurrentPlayer(self, currentPlayer):
    self.currentPlayer = currentPlayer
  def getCurrentPlayer(self):
    return self.currentPlayer
  def setLastMove(self, lastMove):
    self.lastMove = lastMove
  def getLastMove(self):
    return self.lastMove
  def addPossibleMove(self, newPossibleMove):
    self.possibleMoves.append(newPossibleMove)
  def getPossibleMoves(self):
    return self.possibleMoves
  def clone(self): # returns a clone of itself
    gameStateClone = GameState(self.getCheckersBoard(), self.getCurrentPlayer(),
                               self.getLastMove())
    for eachMove in self.getPossibleMoves():
      gameStateClone.addPossibleMove(eachMove)
    return gameStateClone
  def __iter__(self):
    if(self.possibleMoves == )
    return iter(self.possible_moves)
  def getAvailableMoves(self):
    for player in self.getCheckersBoard().observers:
        for piece in player.getPlayerPieces():
            for moveType in ['moveLeft', 'moveRight', 'jumpLeft', 'jumpRight']:
                if self.getCheckersBoard().isValidMove(player, piece.getLocation(), moveType):
                    self.possible_moves.append((piece, moveType))
