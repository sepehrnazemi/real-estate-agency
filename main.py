import sqlite3

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)

db = sqlite3.connect('sql.db')
cursor = db.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([name] TEXT, [username] TEXT, [password] TEXT)
          ''')
          
cursor.execute('''
          CREATE TABLE IF NOT EXISTS admins
          ([name] TEXT, [username] TEXT, [password] TEXT)
          ''')
db.commit()

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
            break
        elif order == "exitexit":
            exit()
            
def pre_singin():
    pass

def pre_singup():
    while end != True:
        order = input()
        if order == "1":
            singup("users")
        elif order == "2":
            singup("admins")
        elif order == "exit":
            break
        elif order == "exitexit":
            exit()
            
def singup(n):
    while end != True:
        name = input()
        username = input()
        db_order = "SELECT * FROM {table_name} WHERE username = {table_username}".format(table_name = n, table_username = username)
        cursor.execute(db_order)
        if cursor.fetchall() != []:
            print("Repeated username!")
            continue
        password = input()
        
