import sqlite3
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
#import decimal

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        cursor.execute("SELECT * FROM USERS WHERE username = %r" %(self.username))
        movaghat = cursor.fetchall()
        if movaghat == []:
            self.credit = 0
        else:
            self.credit = movaghat[0][3]
    
    def rename(self, type):
        while True:
            order = input("Enter your new name:\n")
            if order == "exit":
                break
            elif order == "exitexit":
                exit()
            self.name = order
            cursor.execute("UPDATE %r SET name = %r WHERE username = %r" %(type, order, self.username))
            db.commit()
            break

    def newpassword(self, type):
        while True:
            order = input("Enter your new password:\n")
            if order == "exit":
                break
            elif order == "exitexit":
                exit()
            self.password = order
            cursor.execute("UPDATE %r SET password = %r WHERE username = %r" %(type, order, self.username))
            db.commit()
            break

    def update_credit(self, type):
        while True:
            order = input("Enter your number:\n")
            if order == "exit":
                break
            elif order == "exitexit":
                exit()
            elif order.isdecimal() == False:
                print("You didn't enter the number!")
                continue
            self.credit += int(order)
            cursor.execute("UPDATE %r SET cedit = %r WHERE username = %r" %(type, self.credit, self.username))
            db.commit()
            break

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

db = sqlite3.connect('sql.db')
cursor = db.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([name] TEXT, [username] TEXT, [password] TEXT, [credit] INTEGER)
          ''')
          
cursor.execute('''
          CREATE TABLE IF NOT EXISTS admins
          ([name] TEXT, [username] TEXT, [password] TEXT, [credit] INTEGER)
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS buying_homes
          ([id] INTEGER PRIMARY KEY, [price] INTEGER, [address] TEXT, [construct_year] TEXT,
           [roooms_number] INTEGER, [parkings_number] INTEGER,
           [furnished] TEXT, [seler_username] TEXT, [buyer_username] TEXT, [status] TEXT)
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS renting_homes
          ([id] INTEGER PRIMARY KEY, [security_deposit] INTEGER, [monthly_rent] INTEGER, [address] TEXT, [construct_year] TEXT,
           [roooms_number] INTEGER, [parkings_number] INTEGER, [furnished] TEXT, [period] INTEGER,
           [start_date] TEXT, [end_date] TEXT, [owner_username] TEXT, [renter_username] TEXT,[payed_monthes] INTEGER ,[status] TEXT)
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS real_estate
          ([id] INTEGER PRIMARY KEY, [password] TEXT, [credit] INTEGER)
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS transactions
          ([id] INTEGER PRIMARY KEY, [credit] INTEGER, [reason] TEXT, [functor] TEXT)
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
        username = input("Enter your usename:\n")
        if username == "exit":
            break
        elif username == "exitexit":
            exit()
        password = input("Enter your password:\n")
        cursor.execute("SELECT password FROM %r WHERE USERNAME = %r" %(n, username))
        if cursor.fetchall()[0][0] != password:
            print("Incorrect username or password!")
            continue
        cursor.execute("SELECT name FROM %r WHERE USERNAME = %r" %(n, username))
        global user
        user = User(cursor.fetchall()[0][0], username, password)
        if n == "USERS":
            user_menu()
        else:
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
        cursor.execute(" INSERT INTO %r VALUES (%r, %r, %r, 0)" %(n, name, username, password))
        db.commit()
        global user
        user = User(name, username, password)
        if n == "USERS":
            user_menu()
        else:
            admin_menu()

def user_menu():
    while end != True:
        order = input('''Choose operation:\n1-buying home\n2-renting homes
        3-deletacount\n4-rename\n5-myhomes\n6-buying user
        7-update data\n8-change password\n9-rent homes\ncheck creadit''')
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        elif order == "1":
            home_menu()

def admin_menu():
    pass#todo

def home_menu():
    while True:
        order = input("Choose operation:\n1- Add \n2- Choose\n3- Show:")
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        elif order == "3":
            show_home("buying_homes")

li = ["id", "price" ,"address", "construct_year", "roooms_number", "parkings_number", "furnished", "seler_username", "buyer_username", "status"]

def show_home(n):
    while True:
        if n == "buying_homes":
            order = input("Enter sort mudel:id/price/construct_year/roooms_number/parkings_number/furnished")
            if order == "exit":
                break
            elif order == "exitexit":
                exit()
            sort_type = input("Choose sort type:\n1- descending\n2- ascending")
            if sort_type == "1":
                cursor = db.execute("SELECT * FROM buying_homes ORDER BY %r DESC" %(order))
                df = pd.DataFrame(cursor.fetchall(), columns=li)
                print(df)
            else:
                cursor = db.execute("SELECT * FROM buying_homes ORDER BY %r ASC" %(order))
                df = pd.DataFrame(cursor.fetchall(), columns=li)
                print(df)
            
first()
