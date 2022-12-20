import sqlite3
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import pandas as pd

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
            fil = open("user.txt", "r")
            li = fil.readline()
            fil.close()
            li[0] = self.name + "\n"
            fil = open("user.txt", "w")
            fil.writelines(li)
            fil.close()
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
            fil = open("user.txt", "r")
            li = fil.readline()
            fil.close()
            li[2] = self.password + "\n"
            fil = open("user.txt", "w")
            fil.writelines(li)
            fil.close()
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
            cursor.execute("UPDATE %r SET cedit = %d WHERE username = %r" %(type, self.credit, self.username))
            db.commit()
            break

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
          ([id] INTEGER PRIMARY KEY, [price] INTEGER, [address] TEXT, [area_size] REAL, [construct_year] TEXT,
           [roooms_number] INTEGER, [parkings_number] INTEGER,
           [furnished] TEXT, [seler_username] TEXT, [requesters] TEXT, [buyer_username] TEXT, [date_added] TEXT, [date_sold] TEXT, [status] TEXT)
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS renting_homes
          ([id] INTEGER PRIMARY KEY, [security_deposit] INTEGER, [monthly_rent] INTEGER, [address] TEXT, [area_size] REAL,
           [construct_year] TEXT, [roooms_number] INTEGER, [parkings_number] INTEGER, [furnished] TEXT, [period] INTEGER,
           [start_date] TEXT, [end_date] TEXT, [owner_username] TEXT, [requesters] TEXT, [renter_username] TEXT, [payed_monthes] INTEGER, [date_added] TEXT, [status] TEXT)
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS real_estate
          ([id] INTEGER PRIMARY KEY, [password] TEXT, [credit] INTEGER)
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS transactions
          ([id] INTEGER PRIMARY KEY, [date] TEXT, [credit] INTEGER, [reason] TEXT, [functor] TEXT)
          ''')

db.commit()

cursor.execute("SELECT * FROM real_estate WHERE id = 1")
movaghat = cursor.fetchall()
if movaghat == []:
    cursor.execute(" INSERT INTO real_estate(password, credit) VALUES ('0000', 0)")
    db.commit()
    important_password = "0000"
else:
    important_password = movaghat[0][1]
    
b_homes_columns = ["id", "price" , "address", "area_size", "construct_year", "roooms_number",
                   "parkings_number", "furnished", "seler_username", "requesters", "buyer_username", "date_added", "date_sold", "status"]
r_homes_columns = ["id", "security_deposit","monthly_rent" , "address", "area_size", "construct_year", "roooms_number",
                   "parkings_number", "furnished", "period", "start_date", "end_date",
                    "owner_username", "requesters", "renter_username", "payed_monthes", "date_added", "status"]
user = User(0, "0", 0)

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
        li = cursor.fetchall()[0]
        user = User(li[0], username, password)
        fil = open("user.txt", "w")
        fil.writelines([user.name, "\n", user.username, "\n", user.password, "\n"])
        fil.close()
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
        if n == "admins":
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
        cursor.execute("INSERT INTO %r VALUES (%r, %r, %r, 0)" %(n, name, username, password))
        db.commit()
        global user
        user = User(name, username, password)
        fil = open("user.txt", "w")
        fil.writelines([user.name, "\n", user.username, "\n", user.password, "\n"])
        fil.close()
        if n == "users":
            user_menu()
        else:
            admin_menu()

def user_menu():
    while end != True:
        order = input('''Choose operation:\n1- Buying home\n2- Renting home\n3- Check credit
4- Update credit\n5- My homes\n6- Check rentings\n7- Rename\n8- Change password\n9- Sing out\n10- Delete account''')
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        elif order == "1":
            home_menu("buying_homes")
        elif order == "2":
            home_menu("renting_homes")
        elif order == "3":
            check_credit()
        elif order == "4":
            user.update_credit(check_user(user.username))
        elif order == "5":
            user_homes()
        elif order == "6":
            renting_menu()
        elif order == "7":
            user.rename(check_user(user.username))
        elif order == "8":
            user.newpassword(check_user(user.username))
        elif order == "9":
            singout()
        elif order == "10":
            deleteac()

def check_credit():
    cursor.execute("SELECT * FROM %r WHERE username = %r" %(check_user(user.username), user.username))
    user.credit = cursor.fetchall()[0][3]
    print(user.credit)

def singout():
    global user
    user = User(0, "0", 0)
    global end
    end = True
    print("\U0001F44B")

def deleteac(username):
    user_type = check_user(username)
    cursor.execute("SELECT * FROM renting_homes WHERE renter_username = %r OR owner_username = %r AND status = 'Inactive'" %(user.username, user.username))
    if cursor.fetchall != []:
        for i in cursor.fetchall:
            if i[9] != i[14]:
                print("Having renting!")
                return None
    elif user.credit < 0:
        print("Didn't pay money!")
        return None
    cursor.execute("DELETE FROM %r WHERE username = %r" %(user_type, username))
    cursor.execute("DELETE FROM buying_homes WHERE seler_username = %r AND status = 'Active'" %(username))
    cursor.execute("DELETE FROM renting_homes WHERE owner_username = %r AND status = 'Active'" %(username))
    db.commit()
    print("\U0001F44B")
    global end
    end = True

def admin_menu():
    pass#TODO

def home_menu(n):
    while True:
        order = input("Choose operation:\n1- Add \n2- Choose home\n3- Choose request\n3- Show\n")
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        elif order == "1":
            add_home(n)
        elif order == "2":
            add_request()
        elif order == "3":
            choose_request(n)
        elif order == "4":
            show_home(n)
            
def add_home(n):
    while True:
        address = input("Enter the address:\n")
        if address == "exit":
            break
        elif address == "exitexit":
            exit()
        elif n == "buying_homes":
            if unique_home(address) == False:
                print("Repeated home!")
                continue
            price = int(input("Enter price:\n"))
            area = float(input("Enter the area size:\n"))
            construct_year = int(input("Enter construct year:\n"))
            roooms_number = int(input("Enter roooms number:\n"))
            parkings_number = int(input("Enter parkings number:\n"))
            furnished = input("Is it furnished?(yes/no)\n")
            cursor.execute(" INSERT INTO buying_homes VALUES (null, %d, %r, %f, %r, %d, %d, %r, %r, %r, %r, %r, %r)" %(price, address, area, construct_year, roooms_number, parkings_number, furnished, user.username, "unknown", str(datetime.today()).replace(second=0, microsecond=0), "unknown", "Waiting"))
            db.commit()
        elif n == "renting_homes":
            if unique_home(address) == False:
                print("Repeated home!")
                continue
            monthly_rent = int(input("Enter the monthly rent:\n"))
            period = int(input("Enter the period months:\n"))
            security_deposit = int(input("Enter the security deposit:\n"))
            if security_deposit < monthly_rent * period:
                print("Security deposit can't be less than: monthly rent * period.")
                continue
            area = float(input("Enter the area size:\n"))
            construct_year = int(input("Enter construct year:\n"))
            roooms_number = int(input("Enter roooms number:\n"))
            parkings_number = int(input("Enter parkings number:\n"))
            furnished = input("Is it furnished?(yes/no)\n")
            cursor.execute(" INSERT INTO renting_homes VALUES (null, %d, %d, %r, %f, %r, %d, %d, %r, %d, %r, %r, %r, %r, %d, %r, %r)" %(security_deposit, monthly_rent, address, area, construct_year, roooms_number, parkings_number, furnished, period, "unknown", "unknown", user.username, "unknown", 0, str(datetime.today()).replace(second=0, microsecond=0), "Waiting"))
            db.commit()
            
def unique_home(n):
    cursor.execute("SELECT * FROM buying_homes WHERE address = %r" %(n))
    movaghat = cursor.fetchall()
    cursor.execute("SELECT * FROM renting_homes WHERE address = %r" %(n))
    if cursor.fetchall() != [] or movaghat != []:
        return False
    else: return True 

def add_request(n):
    while True:
        order = input("Enter the id:\n")
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        elif order.isdecimal() == False:
            print("You didn't enter the number!")
        elif n == "buying_homes":
            cursor.execute("SELECT * FROM buying_homes WHERE id = %d AND status = 'Active'" %(id))
            home = cursor.fetchall()
            if home == []:
                print("No active home with this id!")
                continue
            buyer_username = home[9]
            if user.username in buyer_username:
                print("You sent the request!")
                continue
            if buyer_username == "":
                buyer_username += user.username
            else:
                buyer_username += (", " + user.username)
            cursor.execute("UPDATE buying_homes SET requesters = %r WHERE id = %d" %(buyer_username, id))
        elif n == "renting_homes":
            cursor.execute("SELECT * FROM renting_homes WHERE id = %d AND status = 'Active'" %(id))
            home = cursor.fetchall()
            if home == []:
                print("No active home with this id!")
                continue
            renter_username = home[13]
            if user.username in renter_username:
                print("You sent the request!")
                continue
            if renter_username == "":
                renter_username += user.username
            else:
                renter_username += (", " + user.username)
            cursor.execute("UPDATE renting_homes SET requesters = %r WHERE id = %d" %(renter_username, id))

def remove_request(n):
    while True:
        order = input("Enter the id:\n")
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        elif order.isdecimal() == False:
            print("You didn't enter the number!")
        elif n == "buying_homes":
            cursor.execute("SELECT * FROM buying_homes WHERE id = %d AND status = 'Active'" %(id))
            home = cursor.fetchall()
            if home == []:
                print("No active home with this id!")
                continue
            buyer_username = home[9].split(", ")
            if user.username not in buyer_username:
                print("You didn't request!")
                continue
            buyer_username.remove(user.username)
            buyer_username = str(buyer_username)
            buyer_username = buyer_username.replace("[", "")
            buyer_username = buyer_username.replace("]", "")
            buyer_username = buyer_username.replace("'", "")
            cursor.execute("UPDATE buying_homes SET requesters = %r WHERE id = %d" %(buyer_username, id))
            db.commit()
        elif n == "renting_homes":
            cursor.execute("SELECT * FROM renting_homes WHERE id = %d AND status = 'Active'" %(id))
            home = cursor.fetchall()
            if home == []:
                print("No active home with this id!")
                continue
            renter_username = home[13].split(", ")
            if user.username not in renter_username:
                print("You didn't request!")
                continue
            renter_username.remove(user.username)
            renter_username = str(renter_username)
            renter_username = renter_username.replace("[", "")
            renter_username = renter_username.replace("]", "")
            renter_username = renter_username.replace("'", "")
            cursor.execute("UPDATE buying_homes SET requesters = %r WHERE id = %d" %(renter_username, id))
            db.commit()

def active_home(n: str):
    order = input("Enter the id:\n")
    if order == "exit":
        return None
    elif order == "exitexit":
        exit()
    elif order.isdecimal() == False:
        print("You didn't enter the number!")
        return None
    cursor.execute("UPDATE %s SET requesters = 'Active' WHERE id = %d" %(n, id))
    db.commit()

def choose_request(n):
    global user
    while True:
        id = input("Enter the id:\n")
        if id == "exit":
            break
        elif id == "exitexit":
            exit()
        elif id.isdecimal() == False:
            print("You didn't enter the number!")
            continue
        id = int(id)
        username = input("Enter the username:\n")
        if n == "buying_homes":
            cursor.execute("SELECT * FROM buying_homes WHERE id = %d AND status = 'Active'" %(id))
            home = cursor.fetchall()
            if home == []:
                print("No active home with this id!")
                continue
            buyer_usernames = home[9]
            if username not in buyer_usernames:
                print("Enter correct username!")
                continue
            home = home[0]
            price = home[1]
            cursor.execute("SELECT * FROM %s WHERE username = %r" %(check_user(username), username))
            li = cursor.fetchall()[0]
            buyer_credit = li[3]
            if buyer_credit < price:
                print("The credit isn't enough!")
                continue
            utype = check_user(user.username)
            buyer_credit -= price
            cursor.execute("UPDATE %s SET credit = %d WHERE username = %r" %(check_user(username), buyer_credit, username))
            cursor.execute("SELECT * FROM real_estate WHERE id = 1")
            price_program = cursor.fetchall()[0][2]
            movaghat = price // 100
            price_program += movaghat
            user.credit += (price - movaghat)
            cursor.execute("UPDATE %s SET credit = %d WHERE username = %r" %(utype, user.credit, user.username))
            cursor.execute("UPDATE real_estate SET credit = %d WHERE id = 1" %(price_program))
            cursor.execute("UPDATE buying_homes SET requesters = 'Inactive' WHERE id = %d" %(id))
            cursor.execute("UPDATE buying_homes SET status = 'Inactive' WHERE id = %d" %(id))
            cursor.execute("UPDATE buying_homes SET buyer_username = %r WHERE id = %d" %(username, id))
            cursor.execute("UPDATE buying_homes SET date_sold = %r WHERE id = %d" %(str(date.today()), id))
            cursor.execute(" INSERT INTO transactions VALUES (null ,%r, %d, 'buying home', %r)" %(str(datetime.today()).replace(second=0, microsecond=0), price_program, user.username))
            db.commit()
        elif n == "renting_homes":
            cursor.execute("SELECT * FROM renting_homes WHERE id = %d AND status = 'Active'" %(id))
            home = cursor.fetchall()
            if home == []:
                print("No active home with this id!")
                continue
            home = home[0]
            security_deposit = home[1]
            buyer_usernames = home[13]
            if username not in buyer_usernames:
                print("Enter correct username!")
                continue
            cursor.execute("SELECT * FROM %s WHERE username = %r" %(check_user(username), username))
            li = cursor.fetchall()[0]
            renter_credit = li[3]
            if renter_credit < security_deposit:
                print("Your credit isn't enough!")
                continue
            renter_credit -= security_deposit
            price_program = security_deposit // 100
            user.credit += (security_deposit - price_program)
            cursor.execute("UPDATE %s SET credit = %d WHERE username = %r" %(check_user(user.username) , user.credit, user.username))
            cursor.execute("UPDATE %s SET credit = %d WHERE username = %r" %(check_user(username) , renter_credit, username))
            cursor.execute("UPDATE renting_homes SET status = 'Inactive' WHERE id = %d" %(id))
            cursor.execute("UPDATE renting_homes SET requesters = 'Inactive' WHERE id = %d" %(id))
            cursor.execute("UPDATE renting_homes SET start_date = %r WHERE id = %d" %(str(date.today()), id))
            period = home[9]
            cursor.execute("UPDATE renting_homes SET end_date = %r WHERE id = %d" %(str(date.today() + relativedelta(months=period)), id))
            cursor.execute("UPDATE renting_homes SET renter_username = %r WHERE id = %d" %(username, id))
            cursor.execute("SELECT * FROM real_estate WHERE id = 1")
            movaghat = cursor.fetchall()[0]
            price += movaghat[2]
            cursor.execute("UPDATE real_estate SET credit = %d WHERE id = 1" %(price))
            cursor.execute("INSERT INTO transactions VALUES (null, %r, %d, 'renting home', %r)" %(n, str(datetime.today()).replace(second=0, microsecond=0), price_program, user.username))
            db.commit()

def  renting_menu():
    while True:
        order = input("Choose type:\n1- By home id\n2- My rentings")
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        elif order == "1":
            id = input("Enter the id:\n")
            check_rent(id)
        elif order == "2":
            check_rents(user.username)

def check_rents(username):
    li = []
    n = 0
    cursor.execute("SELECT * FROM renting_homes WHERE owner_username = %r AND status = 'Inactive'" %(username))
    li.extend(cursor.fetchall)
    cursor.execute("SELECT * FROM renting_homes WHERE renter_username = %r AND status = 'Inactive'" %(username))
    li.extend(cursor.fetchall())
    if li == []:
        print("You don't have any rentings")
        return None
    for i in li:
        if i[9] != i[14]:
            check_rent(i[0])
            n += 1
    if n == 0:
        print("Your rentings are finished.")

def check_rent(id) -> None:
    cursor.execute("SELECT * FROM renting_homes WHERE id = %d AND status = 'Inactive'" %(id))
    home = cursor.fetchall()
    if home == []:
        print("No rented home with this id!")
        return None
    home = home[0]
    period = home[9]
    payed_monthes = home[14]
    if payed_monthes == period:
        print("The home paying is finished!")
        return None
    started = home[10]
    started = started.split()
    started = [int(i) for i in started]
    started = date(started[0], started[1], started[2])
    li = []
    security_deposit = home[1]
    monthly_rent = home[2]
    owner_type = check_user(home[12])
    cursor.execute("SELECT * FROM %r WHERE username = %r" %(owner_type, home[12]))
    owner = cursor.fetchall()[0]
    renter_type = check_user(home[13])
    cursor.execute("SELECT * FROM %r WHERE username = %r" %(renter_type, home[13]))
    renter = cursor.fetchall()[0]
    time = 0
    owner_credit = owner[3]
    renter_credit = renter[3]
    for i in range(1, period+1):
        h = started + relativedelta(months=+i)
        li.append(h)
    for i in li:
        if i <= date.today():
            time += 1
        else:
            break
    monthes = time - payed_monthes
    payed_monthes = time
    cursor.execute("UPDATE renting_homes SET payed_monthes = %d WHERE id = %d" %(payed_monthes, id))
    paying = monthes * monthly_rent
    renter_credit -= paying
    owner_credit += paying
    if payed_monthes == period:
        renter_credit += security_deposit
        owner_credit -= security_deposit
    cursor.execute("UPDATE %r SET credit = %d WHERE username = %r" %(renter_type , renter_credit, renter[1]))
    cursor.execute("UPDATE %r SET credit = %d WHERE username = %r" %(owner_type , owner_credit, owner[1]))
    db.commit()    

def check_user(n):
    cursor.execute("SELECT * FROM users WHERE username = %r" %(n))
    if cursor.fetchall == []:
        return 'admins'
    else:
        return 'users'

def show_home(n):
    while True:
        filter1 = 'status'
        filter2 = "Active"
        name = n
        type = input("Choose sort type:\n1- Descending\n2- Ascending\n")
        if type == "exit":
            break
        elif type == "exitexit":
            exit()
        if n == "buying_homes":
            sort = input("Enter sort mudel:id/price/address/area_size/construct_year/roooms_number/parkings_number/furnished\n")
            table_d(name, filter1, filter2, sort, type)
        elif n == "renting_homes":
            sort = input("Enter sort mudel:id/security_deposit/monthly_rent/address/period/area_size/construct_year/roooms_number/parkings_number/furnished\n")
            table_d(name, filter1, filter2, sort, type)

def user_homes():
    while True:
        order = input("Enter type:seler/buyer/owner/renter\n")
        if order == "exit":
            break
        elif order == "exitexit":
            exit()
        filter1 = order + "_username"
        filter2 = user.username
        type = input("Choose sort type:\n1- Descending\n2- Ascending\n")
        if order == "seler" or order == "buyer":
            name = 'buying_homes'
            sort = input("Enter sort mudel:id/price/address/area_size/construct_year/roooms_number/parkings_number/furnished\n")
            table_d(name, filter1, filter2, sort, type)
        elif order == "owner" or order == "renter":
            name = 'renting_homes'
            sort = input("Enter sort mudel:id/security_deposit/monthly_rent/address/period/area_size/construct_year/roooms_number/parkings_number/furnished\n")
            table_d(name, filter1, filter2, sort, type)


def table_d(name, filter: str, filter2, sort, type):
    if type == 1:
        cursor.execute("SELECT * FROM %r WHERE %s = %r ORDER BY %s DESC" %(name, filter, filter2, sort))
    else:
        cursor.execute("SELECT * FROM %r WHERE %s = %r ORDER BY %s ASC" %(name, filter, filter2, sort))
    if name == "buying_homes":
        df = pd.DataFrame(cursor.fetchall(), columns=b_homes_columns)
    else:
        df = pd.DataFrame(cursor.fetchall(), columns=b_homes_columns)
    df.set_index('id', inplace = True)
    print(df)

try:
    fil = open("user.txt", "r")
    li = fil.readline()
    li = [i.strip() for i in li]
    fil.close()
    cursor.execute("SELECT * FROM %s WHERE username = %r" %(check_user(li[1]), li[1]))
    pre_user = cursor.fetchall()
    if pre_user == []:
        first()
    else:
        if pre_user[0][2] != li[2]:
            first()
        else:
            user = User(li[0], li[1], li[2])
            if check_user(li[1]) == 'users':
                user_menu()
            else:
                admin_menu()
except:
    first()
