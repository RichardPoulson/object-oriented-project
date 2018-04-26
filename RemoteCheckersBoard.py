from GameObservable import *
from Space import *
from CheckersBoard import *
import numpy as np

class RemoteCheckersBoard(CheckersBoard):

    def __init__(self, server):
        super(RemoteCheckersBoard, self).__init__()
        self.server = server

    def getServer(self):
        return self.server

    def broadcastState(self):
        self.server.sendState(self.getReadOnlyState())
