class View:
    def __init__(self):
        pass

    def displayStartScreen(self):
        print("Welcome to Checkers!")
        print("")
        print("Would you like to (1) login or (2) create a new account?")
        userInput = int(input(">"))
        return userInput

    def displayLogon(self):
        username = input("user name: ")
        password = input("password: ")
        return (username, password)

    def displayRegister(self):
        username = input("Select a user name: ")
        password = input("Select your password: ")
        return (username, password)

    def displayMenu(self):
        print('MAIN MENU')
        print('---------')
        print('(1) Play Against AI')
        print('(2) Host Game')
        print('(3) Join Game')
        print('(4) View System Rankings')
        print('(5) View System Usage')
        print('(6) Help')
        print('(7) Quit')
        print('')
        userInput = int(input("Enter Selection> "))
        return userInput

    def displayAddressPortForm(self, action):
        address = input('Enter Address for game {}: '.format(action))
        port = int(input('Enter Port for game {}: '.format(action)))
        return (address, port)

    def getPlayerMove(self, playerType):
        if (playerType == 'HumanPlayer'):
            pieceID = input("pieceID: ")
            moveType = input("moveType: ")
        elif (playerType == 'ComputerPlayer'):
            pieceID = None
            moveType = None
        return (pieceID, moveType)

    def displayBoard(self, readOnlyBoard):
        for row in readOnlyBoard:
            print(row)
        print()

    def displayStatus(self, statusMsg):
        print(statusMsg)

    def displayHelp(self):
        helpFile = open('../help.txt', encoding="ISO-8859-1")
        for line in helpFile.readlines():
            print(line)

    def displayRankings(self, ranks):
        print("User, Wins, Losses")
        print("------------------")
        for ranking in ranks:
            print("{}, {}, {}".format(ranking[0], ranking[1], ranking[2]))
        print()

    def displayUsage(self, playTimes):
        print("User, Play Time")
        print("------------------")
        for playtime in playTimes:
            print("{}, {}".format(playtime[0], playtime[1]))
        print()
