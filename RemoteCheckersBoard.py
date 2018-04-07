from GameObservable import *
from PieceFactory import *
from Space import *
from PieceFactory import *
from CheckersBoard import *
import numpy as np

class RemoteCheckersBoard(CheckersBoard):

    def __init__(self, server):
        super(RemoteCheckersBoard, self).__init__()
        self.server = server

    def getServer(self):
        return self.server

    def movePlayerPiece(self, piece, player, currentLocation, moveType):
        self.setMoveStrategy(self.moveStrategyFactory.getMoveStrategy(player.id, moveType))
        vertical, horizontal = self.getMoveStrategy().locationChange()
        if self.isValidMove(player, currentLocation, moveType):
            if (moveType == 'jumpLeft' or moveType == 'jumpRight'):
                # remove opponent piece, move piece
                jumpedSpace = self.getSpaceByLocation(int(currentLocation[0]+vertical/2),  int(currentLocation[1]+horizontal/2))
                #TODO: decrement opponent player's piececount
                jumpedSpace.getSpaceResident().getOwner().decrementNumPieces()
                jumpedSpace.removeSpaceResident()

            self.getSpaceByLocation(currentLocation[0], currentLocation[1]).removeSpaceResident()
            self.getSpaceByLocation(currentLocation[0]+vertical, currentLocation[1]+horizontal).setSpaceResident(piece)
            currentLocation = (currentLocation[0]+vertical, currentLocation[1]+horizontal)
        else:
            print('invalid move')

        return currentLocation

    def broadcastState(self):
        self.server.sendState(self.getReadOnlyState())
