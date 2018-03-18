from AbstractPlayer import *
from CheckersPiece import *
import socket

class HumanPlayer(AbstractPlayer):
    def __init__(self, playerID=None):
        self._id = playerID
        self._pieces = {}
        self._numPieces = 0
        self.playerSocket = socket.socket()

    def addToPieceCollection(self, newPieceID, newPiece):
        self._pieces[newPieceID] = newPiece

    def getPieceFromCollection(self, pieceID):
        return self._pieces[pieceID]

    def getNumPieces(self):
        return self._numPieces

    def setNumPieces(self):
        self._numPieces = len(self._pieces)

    def decrementNumPieces(self):
        self._numPieces -= 1

    def getPlayerSocket(self):
        return self.playerSocket

    def connectPlayerSocket(self, address, port):
        self.playerSocket.connect((address, port))

    def makeMove(self, gameBoard, pieceID, moveType):
        self._pieces[pieceID].movePiece(gameBoard, self, moveType)

    def update(self, gameBoard):
        gameBoard.printBoard()
