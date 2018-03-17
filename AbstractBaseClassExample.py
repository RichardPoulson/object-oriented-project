# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/abc.html
"""
from abc import ABCMeta, abstractmethod

class aiDecision(metaclass=ABCMeta):
  @abstractmethod
  def getNextMove(self):
    pass
  @abstractmethod
  def updateKnowledge(self):
    pass
  
class Decision(aiDecision):
  def __init__(self, name):
    self.name = name
    self.age = 0
  #== un-comment the methods below to make TypeError go away
  #def getNextMove(self):
  #  return ""
  #def updateKnowledge():
  #  return ""
  def __str__(self):
    return self.name

myDecision = Decision("John")
print(myDecision)
      


    