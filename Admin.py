import sqlite3

class Admin(object):
	# def __init__(self, username=None, password=None, controller=None, dbClient=None):
	# 	self.username = username
	# 	self.password = password
	# 	self.controller = controller
	# 	self.dbClient = dbClient
	def __init__(self, controller=None, dbClient=None):
		self.controller = controller
		self.dbClient = dbClient


	def register(username, password):
		return 0

	def login(username, password):
		while True:
			username = input("Please enter your username: ")
			password = input("Please enter your password: ")
			#make connection
			with sqlite3.connect("Login.db") as db:
				#cursor will run the querys
				cursor = db.cursor
			user_select = ("SELECT * FROM useres WHERE username=? AND password=?")
			cursor.execute(user_select,[(username),(password)])
			results = cursor.fetchall()

			if results:
				for i in results:
					print("Hello ", i[2])
				break
			else:
				print("Username or Password not recognized")
				redo = input("Would you like to try again? Press n to exit")
				if(redo.lower() == "n"):
					print("Login failed")
					time.sleep(1)
					break









    