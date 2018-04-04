# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/abc.html
"""
from Event import Event

class PieceCaptureEvent(Event):
  def __init__(self, piece):
    self.piece = piece
  def getPiece(self):
    return self.piece