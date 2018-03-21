# Testing
from Server import *
from ClientSocket import *
from CheckersBoard import *

import time

server = Server(socket.gethostbyname(''), 10000, CheckersBoard())
server.run()
c = ClientSocket(socket.gethostbyname(''), 10000, 1)
c2 = ClientSocket(socket.gethostbyname(''), 10000, 2)
time.sleep(1)
c.sendMessage(input("Message 1: "))
c.receiveMessage()
c2.receiveMessage()
c2.sendMessage(input("Message 2: "))
c.receiveMessage()
c2.receiveMessage()

server.sendState()
x = c.fetchState()
y = c2.fetchState()
for row in x:
    print(row)

c.clientSocket.close()
c2.clientSocket.close()
server.serverSocket.close()
