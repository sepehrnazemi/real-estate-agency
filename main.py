import sqlite3

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)

def pre_singin():
    pass

def pre_singup():
    pass

def first():
    global end
    end = False
    while True:
        if end == True:
            end = False
        order = input()
        if order == "1":
            pre_singin()
        elif order == "2":
            pre_singup()
        elif order == "exit":
            break()
        elif order == "exitexit":
            exit()
