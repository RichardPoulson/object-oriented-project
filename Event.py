# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/abc.html
"""
from abc import ABCMeta, abstractmethod

class Event(metaclass=ABCMeta):
  @abstractmethod
  def getPiece(self):
    pass