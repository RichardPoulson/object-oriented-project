from CheckersBoard import *
from RemoteCheckersBoard import *
from HumanPlayer import *
from Server import *
from ClientSocket import *
from view.View import *
from DBProxy import *
from DB import *
from User import *

import time


class GameController:
    def __init__(self):
        self.game = None
        self.view = View()
        self.dbProxy = DBProxy(DB())

    def getGame(self):
        return self.game

    def setGame(self, newGame):
        self.game = newGame

    def startApplication(self):
        userInput = self.view.displayStartScreen()

        if (userInput == 1):
            (username, password) = self.view.displayLogon()
            currentUser = User()
            if currentUser.validateLogon(self.dbProxy, username, password):
                self.mainMenu(currentUser)
            else:
                self.startApplication()

        elif (userInput == 2):
            (username, password) = self.view.displayRegister()
            currentUser = User()
            if currentUser.validateRegistration(self.dbProxy, username, password):
                self.mainMenu(currentUser)
            else:
                self.startApplication()

        else:
            self.view.displayStartScreen()

    def mainMenu(self, currentUser):
        userInput = self.view.displayMenu()
        if userInput == 1:
            self.runLocalGame()
        elif userInput == 2:
            (address, port) = self.view.displayAddressPortForm('hosting')
            self.hostGame(currentUser, address, port)
        elif userInput == 3:
            (address, port) = self.view.displayAddressPortForm('joining')
            self.joinGame(currentUser, address, port)
        elif userInput == 4:
            self.view.displayHelp()
        elif userInput == 5:
            return

    def hostGame(self, user, address, port):
        self.setGame(RemoteCheckersBoard(Server(address, port)))
        self.game.getServer().run()
        user.commSocket = ClientSocket(address, port)
        while (self.game.getServer().getNumberOfClientConnections() < 2):
            self.view.displayStatus('waiting for user to join...')
            time.sleep(2)
        self.runRemoteGame(user)

    def joinGame(self, user, address, port):
        user.commSocket = ClientSocket(address, port)
        while True:
            pieceID, moveType = self.view.getPlayerMove()
            user.commSocket.sendCommand(('joiningUser', pieceID, moveType))

    def runRemoteGame(self, user):
        self.game.initializeGameBoard(HumanPlayer(1), HumanPlayer(2))
        self.game.broadcastState()

        while(max(self.game.observers[0].getNumPieces(), self.game.observers[1].getNumPieces()) > 0):
            pieceID, moveType = self.view.getPlayerMove()
            user.commSocket.sendCommand(('hostingUser', pieceID, moveType))

            while (self.game.getServer().getNumberCommandsInQueue('hostingUser') < 1):
                continue

            pieceToMove, moveType = self.game.getServer().commandQueue['hostingUser'].pop(0)

            # TODO: add a method to game to get which observer's turn it is?
            self.game.observers[0].makeMove(self.game, pieceToMove, moveType)
            self.game.broadcastState()

            while (self.game.getServer().getNumberCommandsInQueue('joiningUser') < 1):
                continue

            pieceToMove, moveType = self.game.getServer().commandQueue['joiningUser'].pop(0)
            self.game.observers[1].makeMove(self.game, pieceToMove, moveType)
            self.game.broadcastState()

    def playAI(self, humanPlayer):
        pass

    def runLocalGame(self):
        # TODO: make one of the players an AI player
        self.setGame(CheckersBoard())
        self.game.initializeGameBoard(HumanPlayer(1), HumanPlayer(2))
        self.game.notifyObservers()

        self.view.displayBoard(self.game.getReadOnlyState())

        while(max(self.game.observers[0].getNumPieces(), self.game.observers[1].getNumPieces()) > 0):
            for player in self.game.observers:
                pieceID, moveType = self.view.getPlayerMove()
                player.makeMove(self.game, pieceID, moveType)

                self.view.displayBoard(self.game.getReadOnlyState())
