import pandas as pd
import os

class User:
    def __init__(self, name, last_name, username, password):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, name, last_name, username, password):
        super().__init__(name, last_name, username, password)

if "users.csv" in os.listdir():
    users_file = pd.read_csv("users.csv")
    tags = users_file.to_dict()
    if list(tags.keys()) != ['name', 'last_name', 'username', 'password']:
        os.remove("users.csv")
        users_file = {"name" : [], "last_name" : [],
                  "username" : [], "password" : []}
        users_file = pd.DataFrame(users_file)
        users_file.to_csv("users.csv", index=False)
        users_file = pd.read_csv("users.csv")
else:
    users_file = {"name" : [], "last_name" : [],
                  "username" : [], "password" : []}
    users_file = pd.DataFrame(users_file)
    users_file.to_csv("users.csv", index=False)
    users_file = pd.read_csv("users.csv")

if "admins.csv" in os.listdir():
    admins_file = pd.read_csv("admins.csv")
    tags = admins_file.to_dict()
    if list(tags.keys()) != ['name', 'last_name', 'username', 'password']:
        os.remove("admins.csv")
        admins_file = {"name" : [], "last_name" : [],
                  "username" : [], "password" : []}
        admins_file = pd.DataFrame(users_file)
        admins_file.to_csv("admins.csv", index=False)
        admins_file = pd.read_csv("admins.csv")
else:
    admins_file = {"name" : [], "last_name" : [],
                  "username" : [], "password" : []}
    admins_file = pd.DataFrame(users_file)
    admins_file.to_csv("admins.csv", index=False)
    admins_file = pd.read_csv("admins.csv")
    
important_password = "0000"

end = False
while end != True:
    print("Choose an operation:\n1- Sing in\n2- Sing up\nexit- return\nexitexit- end")
    order = input()
    if order == "1":
        while end != True:
            print("Choose your role:\n1- User\n2- Admin")
            order = input()
            if order == "1":
                pass
            if order == "2":
                pass
            elif order == "exit":
                break
            elif order == "exitexit":
                end = True


    
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
                        end = True
                    order = order.split()
                    users_names = users_file['name'].values.tolist()
                    if order[2] in users_names:
                        print("Repeated username!")
                    else:
                        user = User(order[0], order[1], order[2], order[3])
                        new_user = {"name" : [user.name], "last_name" : [user.last_name],
                            "username" : [user.username], "password" : [user.password]}
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
                            end = True
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
                        end = True
            elif order == "exit":
                break
            elif order == "exitexit":
                end = True

    elif order == "exit":
        break
    elif order == "exitexit":
        end = True

