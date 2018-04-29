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
        # if True:
        #     return True
        # else:
        #     return False
        if(len(dbProxy.executeSelectionQuery("SELECT * FROM useres WHERE username='{}' AND password='{}'".format(username, password))) == 0):
            return False
        else:
            self.username = username
            self.password = password
            return True

    def validateRegistration(self, dbProxy, username, password):
        # if valid, set username and password and return True
        if(len(dbProxy.executeSelectionQuery("SELECT * FROM useres WHERE username='{}'".format(username))) != 0):
            return False
        dbProxy.executeInsertionQuery("INSERT INTO users (username, password, wins, losses, playtime) Values ('{}','{}',0,0,0.0)".format(username, password))
        self.username = username
        self.password = password
        return True
