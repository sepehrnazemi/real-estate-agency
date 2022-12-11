import sqlite3
import datetime
from dateutil.relativedelta import relativedelta

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)

class Home:
    def __init__(self, address, const_year, rooms, parking, furnished, status):
        self.address = address
        self.const_year = const_year
        self.rooms = rooms
        self.parking = parking
        self.status = status
        self.furnished = furnished

class BuyingHome(Home):
    def __init__(self, price, address, const_year, rooms, parking, furnished, seller, buyer, status):
        super().__init__(address, const_year, rooms, parking, furnished, status)
        self.price = price
        self.seller = seller
        self.buyer = buyer

class RentingHome(Home):
    def __init__(self, security_deposit, mo_rent, address, const_year, rooms, parking, furnished, period, start_date, owner, renter, status):
        super().__init__(address, const_year, rooms, parking, furnished, status)
        self.security_deposit = security_deposit
        self.mo_rent = mo_rent
        self.period = period
        if start_date != "unknown":
            start_date = start_date.split(" ")
            self.start_date = datetime(start_date[0], start_date[1], start_date[2])
            self.end_date = self.start_date + relativedelta(months=+int(self.period))
        else:
            self.start_date = "unknown"
            self.end_date = "unknown"
        self.owner = owner
        self.renter = renter
        #check dates again!!!!!

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

important_password = "0000"

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
    while end != True:
        order = input("Choose your role:\n1- User\n2- Admin\n")
        if order == "1":
            singin("USERS")
        elif order == "2":
            singin("ADMINS")
        elif order == "exit":
            break
        elif order == "exitexit":
            exit()

def singin(n):
    while end != True:
        username = input()
        if username == "exit":
            break
        elif username == "exitexit":
            exit()
        password = input()
        cursor.execute("SELECT password FROM %r WHERE USERNAME = %r" %(n, username))
        if cursor.fetchall()[0][0] != password:
            print("Incorrect username or password!")
            continue
        cursor.execute("SELECT name FROM %r WHERE USERNAME = %r" %(n, username))
        if n == "USERS":
            global user
            user = User(cursor.fetchall()[0][0], username, password)
            user_menu()
        else:
            global admin
            admin = Admin(cursor.fetchall()[0][0], username, password)
            admin_menu()
        
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
            
def singup(n):
    while end != True:
        if n == "ADMINS":
            order = input("Enter admins password:\n")
            if name == "exit":
                break
            elif name == "exitexit":
                exit()
            elif order != important_password:
                print("Incorrect password!")
                continue
        name = input("Enter your name:\n")
        if name == "exit":
            break
        elif name == "exitexit":
            exit()
        username = input("Enter your username:\n")
        cursor.execute("SELECT * FROM USERS WHERE username = %r" %(username))
        movaghat = cursor.fetchall()
        cursor.execute("SELECT * FROM ADMINS WHERE username = %r" %(username))
        if cursor.fetchall() != [] or movaghat != []:
            print("Repeated username!")
            del movaghat
            continue
        password = input("Enter your password:\n")
        cursor.execute(" INSERT INTO %r VALUES (%r, %r, %r)" %(n, name, username, password))
        db.commit()
        if n == "USERS":
            global user
            user = User(name, username, password)
            user_menu()
        else:
            global admin
            admin = Admin(name, username, password)
            admin_menu()

def user_menu():
    pass

def admin_menu():
    pass

first()
