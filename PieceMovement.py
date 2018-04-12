# -*- coding: utf-8 -*-

class PieceMovement:
  def __init__(self, piece):
    self.piece = piece
    self.sequenceLocations = []
  def setPiece(self, newPiece):
    self.piece = newPiece
  def getPiece(self):
    return self.piece
  def addLocation(self, location):
    self.sequenceLocations.append(location)
  def getSequenceLocations(self):
    return self.sequenceLocations
  # def __iter__(self):