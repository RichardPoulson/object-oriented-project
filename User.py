class User():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.commSocket = None

    def setCommSocket(self, socket):
        self.commSocket = socket

    def getUsername(self):
        return self.username

    def validateLogon(self, dbProxy, username, password):
        # if valid, set username and password and return True
        if True:
            return True
        else:
            return False

    def validateRegistration(self, dbProxy, username, password):
        # if valid, set username and password and return True
        if True:
            return True
        else:
            return False
