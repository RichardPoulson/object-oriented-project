class View:
    def __init__(self):
        pass

    def displayStartScreen(self):
        print("Welcome to Checkers!")
        print("")
        print("Would you like to (1) login or (2) create a new account?")
        userInput = int(input(">"))
        return userInput

    def getPlayerMove(self):
        pieceID = input("pieceID: ")
        moveType = input("moveType: ")
        return (pieceID, moveType)
