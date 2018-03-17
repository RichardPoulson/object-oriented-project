#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Richard Poulson
Defines the MinMaxNode class

https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
"""

class MinMaxNode:
  # Constructor
  def __init__(self, isMaxNode, value = None):
    self.isMaxNode = isMaxNode    # is this a Max node?
    self.value = value
    self.children = []
  def setValue(self, value):
    self.value = value
  def getValue(self):
    return self.value
  def addChild(self, childNode):
    self.children.append(childNode)
  def isMaxNode(self):
    return self.isMaxNode
  def hasChildren(self):
    return len(self.children) # should be 0 if no children, resulting in false
  def __iter__(self):
    return iter(self.children)
  # used to determine if this MinMaxNode is == to another
  def __eq__(self, other):
    return (self.value == other.value)
  # used to determine if this MinMaxNode is < another
  def __lt__(self, other):
    return (self.value < other.value)
  def __getitem__(self, key):
    for child in self:
      if child.getValue() == key:
        return child