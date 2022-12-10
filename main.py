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
        order = input("Choose an operation:\n1- Sing in\n2- Sing up\nexit- return\nexitexit- end\n")
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
        order = input("Choose your role:\n1- User\n2- Admin\n")
        if order == "1":
            singup("USERS")
        elif order == "2":
            singup("ADMINS")
        elif order == "exit":
            break
        elif order == "exitexit":
            exit()
            
def singup(n): #again
    while end != True:
        name = input()
        if name == "exit":
            break
        elif name == "exitexit":
            exit()
        username = input()
        db_order = "SELECT * FROM %r WHERE username = %r" %(n, username)
        cursor.execute(db_order)
        if cursor.fetchall() != []:
            print("Repeated username!")
            continue
        password = input()
        db_order =" INSERT INTO %r VALUES (%r, %r, %r)" %(n, name, username, password)
        cursor.execute(db_order)
        if n == "USERS":
            global user
            user = User(name, username, password)
            user_menu()
        else:
            order = input("Admins password:\n")
            if order != important_password:
                print("Incorrect password!")
                continue
            global admin
            user = User(name, username, password)
            admin_menu()

def user_menu():
    print("gggg")

def admin_menu():
    pass

first()
