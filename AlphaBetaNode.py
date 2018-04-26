#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Richard Poulson
Defines the AlphaBetaNode.  Includes Alpha and Beta values, used for alpha-beta
pruning when determining the root value of a minimax tree.

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
"""

from sys import maxsize # used to set bounds of node values
# from copy import copy, deepcopy # shallow or deep copy

class AlphaBetaNode:
    def __init__(self, parentNode, value, isMaxNode = True):
        self.parent = parentNode
        self.maxNode = isMaxNode    # is this a Max node?
        self.key = None # at first, it's unknown what the key to the data will be
        self.value = value
        self.move = None
        # assuming system represents integers using two's complement method
        self.children = []
    def getParent(self): return self.parent
    def isMaxNode(self): return self.maxNode
    def setKey(self, key): self.key = key
    def getKey(self): return self.key
    def setMove(self, new_move): self.move = new_move
    def getMove(self): return self.move
    def setValue(self, value): self.value = value
    def getValue(self): return self.value
    def addChild(self, childNode): self.children.append(childNode)
    def hasChildren(self): return len(self.children) # should be 0 if no children, resulting in false
    def __iter__(self): return iter(self.children)
    def __getitem__(self, key):
        for child in self:
            if child.getKey() == key:
                return child