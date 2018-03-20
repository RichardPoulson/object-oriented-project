import socket
import threading
import pickle
from CheckersBoard import *

class ClientSocket:

    def __init__(self, address, port, ID):
        self.id = ID
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((address, port))

    def sendMsg(self):
        while True:
            self.clientSocket.send(bytes(input(""), 'utf-8'))

    def sendMessage(self, message):
        self.clientSocket.send(bytes(message, 'utf-8'))

    def sendCommand(self, command):
        self.clientSocket.send(bytes(command, 'utf-8'))

    def receiveMessage(self):
        data = self.clientSocket.recv(1024)
        print("Client {} recieved: ".format(self.id), str(data, 'utf-8'))

    def fetchState(self):
        newState = self.clientSocket.recv(4096)
        return pickle.loads(newState)
