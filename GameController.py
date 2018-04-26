from CheckersBoard import *
from RemoteCheckersBoard import *
from HumanPlayer import *
from ComputerPlayer import *
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
            self.runLocalGame(currentUser)
            self.mainMenu(currentUser)

        elif userInput == 2:
            (address, port) = self.view.displayAddressPortForm('hosting')
            self.hostGame(currentUser, address, port)

        elif userInput == 3:
            (address, port) = self.view.displayAddressPortForm('joining')
            self.joinGame(currentUser, address, port)

        elif userInput == 4:
            self.view.displayRankings(self.dbProxy.executeSelectionQuery('ranks'))
            self.mainMenu(currentUser)

        elif userInput == 5:
            self.view.displayUsage(self.dbProxy.executeSelectionQuery('playTime'))
            self.mainMenu(currentUser)

        elif userInput == 6:
            self.view.displayHelp()
            self.mainMenu(currentUser)

        elif userInput == 7:
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
            time.sleep(0.5)
            pieceID, moveType = self.view.getPlayerMove('HumanPlayer')
            user.commSocket.sendCommand(('joiningUser', pieceID, moveType))

    def runRemoteGame(self, user):
        self.game.initializeGameBoard(HumanPlayer(1), HumanPlayer(2))
        self.game.broadcastState()

        while(max(self.game.observers[0].getNumPieces(), self.game.observers[1].getNumPieces()) > 0):
            time.sleep(0.5)
            pieceID, moveType = self.view.getPlayerMove('HumanPlayer')
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

    def runLocalGame(self, user):
        # TODO: make one of the players an AI player
        self.setGame(CheckersBoard())
        #self.game.initializeGameBoard(HumanPlayer(1), ComputerPlayer(playerID=2, aiStrategy=None))
        cp = ComputerPlayer(playerID=2)
        cp.setHeuristic(self.getGame())
        cp.setAIStrategy(self.getGame())
        self.game.initializeGameBoard(HumanPlayer(1), cp)
        self.game.notifyObservers()

        self.view.displayBoard(self.game.getReadOnlyState())

        while(self.game.getWinner() is None):
            for player in self.game.observers:
                pieceID, moveType = self.view.getPlayerMove(player.__class__.__name__)
                player.makeMove(self.game, pieceID, moveType)

                self.view.displayBoard(self.game.getReadOnlyState())

        if (type(self.game.getWinner()) == HumanPlayer):
            self.dbProxy.executeUpdateQuery('wins', user, 1)
        else:
            self.dbProxy.executeUpdateQuery('losses', user, 1)

        self.dbProxy.executeUpdateQuery('playtime', user, self.game.getTimerTotal())
