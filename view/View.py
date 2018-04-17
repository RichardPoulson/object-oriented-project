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
        print('(5) Help')
        print('(6) Quit')
        print('')
        userInput = int(input("Enter Selection> "))
        return userInput

    def displayAddressPortForm(self, action):
        address = input('Enter Address for game {}: '.format(action))
        port = int(input('Enter Port for game {}: '.format(action)))
        return (address, port)

    def getPlayerMove(self):
        pieceID = input("pieceID: ")
        moveType = input("moveType: ")
        return (pieceID, moveType)

    def displayBoard(self, readOnlyBoard):
        for row in readOnlyBoard:
            print(row)

    def displayStatus(self, statusMsg):
        print(statusMsg)

    def displayHelp(self):
        helpFile = open('../help.txt', encoding="ISO-8859-1")
        for line in helpFile.readlines():
            print(line)
