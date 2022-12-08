import pandas as pd
import os
import datetime

class User:
    def __init__(self, name, last_name, username, password):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, name, last_name, username, password):
        super().__init__(name, last_name, username, password)
    
def check_file(n: str):
    if "users.csv" in os.listdir():
        file = pd.read_csv(n)
        tags = file.to_dict()
        if list(tags.keys()) != ['name', 'last_name', 'username', 'password']:
            os.remove(n)
            file = {"name" : [], "last_name" : [],
                      "username" : [], "password" : []}
        file = pd.DataFrame(file)
        file.to_csv(n, index=False)
    else:
        file = {"name" : [], "last_name" : [],
                      "username" : [], "password" : []}
        file = pd.DataFrame(file)
        file.to_csv(n, index=False)

def user_menu():
    pass
def sign_in(n: str, username):
    password = input("Enter your password:\n")
    file = pd.read_csv(n)
    file_list = file.values.tolist()
    counter = 0
    for i in file_list:
        if username == i[2] and password == i[3]:
            global person
            person = i
            counter += 1
    if counter == 0:
        return False
    else:
        return True



check_file("users.csv")
check_file("admins.csv")
    
important_password = "0000"

end = False
while True:
    if end == True:
        end = False
    print("Choose an operation:\n1- Sing in\n2- Sing up\nexit- return\nexitexit- end")
    order = input()
    if order == "1":
        while end != True:
            print("Choose your role:\n1- User\n2- Admin")
            order = input()
            if order == "1":
                while end != True:
                    username = input("Enter your username:\n")
                    if username == "exit":
                        break
                    elif username == "exitexit":
                        exit()
                    if sign_in("users.csv", username) == True:
                        user = User(person[0], person[1], person[2], person[3])
                        while end != True:
                            print("TUSHHHHHHHHH")
                    else:
                        print("Incorect password or username")
                
           
            elif order == "2":
                while end != True:
                    username = input("Enter your username:\n")
                    if username == "exit":
                        break
                    elif username == "exitexit":
                        exit()
                    password = input("Enter your password:\n")
                    admins_file = pd.read_csv("admins.csv")
                    admins_list = admins_file.values.tolist()
                    for i in admins_list:
                        if username == i[2] and password == i[3]:
                            admin = Admin(i[0], i[1], i[2], i[3])
                            while end != True:
                                pass
            elif order == "exit":
                break
            elif order == "exitexit":
                exit()


    
    elif order == "2":
        while end != True:
            print("Choose your role:\n1- User\n2- Admin")
            order = input()
            if order == "1":
                while end != True:
                    print("Write your information(name, last name, username, password):")
                    order = input()
                    if order == "exit":
                        break
                    elif order == "exitexit":
                        exit()
                    order = order.split()
                    users_file = pd.read_csv("users.csv")
                    users_names = users_file['name'].values.tolist()
                    if order[2] in users_names:
                        print("Repeated username!")
                    else:
                        user = User(order[0], order[1], order[2], order[3])
                        new_user = {"name" : [str(user.name)], "last_name" : [str(user.last_name)],
                            "username" : [str(user.username)], "password" : [str(user.password)]}
                        new_user = pd.DataFrame(new_user)
                        new_user.to_csv("users.csv", mode='a', index=False, header=False)
                        print("Welcome!")
                        
            elif order == "2":
                while end != True:
                    print("Enter Password:")
                    order = input()
                    if order == important_password:
                        print("Write your information(name, last name, username, password):")
                        order = input()
                        if order == "exit":
                            break
                        elif order == "exitexit":
                            exit()
                        order = order.split()
                        admins_names = admins_file['name'].values.tolist()
                        if order[2] in admins_names:
                            print("Repeated username!")
                        else:
                            admin = Admin(order[0], order[1], order[2], order[3])
                            new_admin = {"name" : [admin.name], "last_name" : [admin.last_name],
                                "username" : [admin.username], "password" : [admin.password]}
                            new_admin = pd.DataFrame(new_admin)
                            new_admin.to_csv("admins.csv", mode='a', index=False, header=False)
                            print("Welcome!")
                        
                    elif order == "exit":
                        break
                    elif order == "exitexit":
                        exit()
            elif order == "exit":
                break
            elif order == "exitexit":
                exit()

    elif order == "exit":
        break
    elif order == "exitexit":
        exit()
