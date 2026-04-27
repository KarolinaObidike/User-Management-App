
#Main menu loop 

def main():
    import user_functions
    active_users = user_functions.load_users("active_users.csv")
    disabled_users = user_functions.load_users("disabled_users.csv")

    while True:
        print("\n1. Add User")
        print("2. View Users")
        print("3. Enable/Disable Users")
        print("4. Test Login")
        print("0. Exit")

        choice = input("Select option: ")
        if choice == "1":
            user_functions.add_user(active_users)
        elif choice == "2":
            user_functions.view_users(active_users, disabled_users)
        elif choice == "3":
            action = input("Type 'disable' or 'enable': ").lower()
            if action == "disable":
                user_functions.disable_user(active_users, disabled_users)
            elif action == "enable":
                user_functions.enable_user(active_users, disabled_users)
        elif choice == "4":
            user_functions.test_login(active_users)
        elif choice == "0":
            user_functions.save_users("active_users.csv", active_users)
            user_functions.save_users("disabled_users.csv", disabled_users)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a valid choice.")

if __name__ == "__main__":
    main()
