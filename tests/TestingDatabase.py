import sys
sys.path.append('../')

from DB import *
from DBProxy import *

db = DB()
dbProxy = DBProxy(db)

results = dbProxy.executeSelectionQuery("SELECT * from users;")
print(results)
print()

dbProxy.executeInsertionQuery("INSERT INTO users (username, password) VALUES ('user3', 'password3');")

results = dbProxy.executeSelectionQuery("SELECT * from users;")
print(results)
