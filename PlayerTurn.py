# -*- coding: utf-8 -*-

class PlayerTurn:
  def __init__(self, currentPlayer):
    self.currentPlayer = currentPlayer
    self.pieceMovement = None
    self.events = []
    def setCurrentPlayer(self, newCurrentPlayer):
      self.currentPlayer = newCurrentPlayer
    def getCurrentPlayer(self):
      return self.currentPlayer
    def setPieceMovement(self, pieceMovement):
      self.pieceMovement = pieceMovement
    def getPieceMovement(self):
      return self.pieceMovement
    def addEvent(self, newEvent):
      self.events.append(newEvent)
    def getEvents(self):
      return self.events