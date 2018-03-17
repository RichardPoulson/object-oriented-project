#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Richard Poulson
Defines the MinMaxNode class, methods for that class, and the
Alpha-Beta pruning algorithm for assigning values MinMaxNodes.

https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
"""

from sys import maxsize # maxsize used to compare other node values
from copy import copy # to make copies of alpha and beta

class AlphaBetaSeach:
  def search(self, node):
    # Find the action that will lead to the state with the highest possible
    # value.
    highest_value = self.maxValue(node, -maxsize-1, maxsize)
    return node[highest_value]
  def maxValue(self, node, alpha, beta):
    if (not node.hasChildren()):    # does this node not need to be evaluated?
      return node.utilityValue()
    current_value = -maxsize - 1    # assign lowest possible value to val
    current_alpha = copy(alpha)
    for child in node:
      temp_value = self.minValue(child, current_alpha, beta)  # get the
      # value and evaluation count from eachChild
      current_value = max(current_value, temp_value)  # update val to the new maximum value
      if (current_value >= beta):  # if this child's value is bigger than val..
        return current_value  # ..Min won't choose 
      current_alpha = max(current_alpha, current_value)
    # found the value for MinMaxNode, so set value
    node.setValue(current_value)
    return current_value
  def minValue(self, node, alpha, beta):
    if (not node.hasChildren()):    # does this node not need to be evaluated?
      return node.utilityValue()
    current_beta = copy(beta)
    current_value = maxsize
    for child in node:
      temporary_value = self.maxValue(child, alpha, current_beta)
      current_value = min(current_value, temporary_value)
      if (current_value <= alpha):
        return current_value
      current_beta = min(current_beta, current_value)
    node.setValue(current_value)
    return current_value