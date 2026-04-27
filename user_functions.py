#Two lists defined

active_users = []
disabled_users = []

#Add user function

def add_user(active_users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = {
        "username": username, 
        "password": password,
        "active": True
    }
    active_users.append(user)

    print(f"User '{username}' added.")

#View users function

def view_users(active_users, disabled_users):
    print("\nActive users:")
    for user in active_users:
        print(user["username"])

    print("\nDisabled Users:")
    for user in disabled_users:
        print(user["username"])

#Disable user function

def disable_user(active_users, disabled_users):
    username = input("Enter username to disable: ")
    
    for user in active_users:
        if user["username"] == username:
            active_users.remove(user)
            disabled_users.append(user)
            print(f"{username} is disabled.")
            return
        print("User not found.")

#Enable user function

def enable_user(active_users, disabled_users):
    username = input("Enter username to enable: ")

    for user in disabled_users:
        if user["username"] == username:
            disabled_users.remove(user)
            active_users.append(user)
            print(f"{username} is enabled.")
            return
        print("User not found.")

#Test login function

def test_login(active_users):
    username = input("Username: ")
    password = input("Password: ")

    for user in active_users:
        if user["username"] == username and user["password"] == password:
            print("Access granted.")
            return 
    print("Access denied.")

#Load users function

import csv 

def load_users(filename):
    users = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["active"] = row.get("active", "True") == "True"
                users.append(row)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty list.")

    return users

#Save users function

def save_users(filename, users):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password", "active"])
        writer.writeheader()
        writer.writerows(users)