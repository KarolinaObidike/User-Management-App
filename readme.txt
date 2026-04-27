USER MANAGEMENT APPLICATION
---------------------------

OVERVIEW
--------
This application is a simple Python command-line User Management system. 

It allows you to:
- Add users
- View your users
- Enable/Disable your users
- Test user login
- Save and load users using CVS files as your database

The system separates users into:
- Active users
- Disabled users

FEATURES
--------
1. Add User:
    - Creates a new user with username and password
    - Stores added user as active, as default
2. View users
    - Displays both active and disabled users
3. Enable/Disable users
    - Moves users between active and disabled states
4. Test login
    - Checks username and password against active users
5. Persistent Storage
    - Users are saved to a CSV files:
        - active_users.CSV
        - disabled_users.CSV

STRUCTURE
---------

main.py 
    - Runs the application
    - Contains the menu system
user_functions.py 
    - Contains all user-related user_functions
    add_user
    view_user
    disable_user
    enable_user
    test_login
    load_users
    save_users

RUNNING INSTRUCTIONS
--------------------

1. Open terminal in User Management App folder
2. Run: python main.py
3. Follow on-screen menu options

NOTES
-----

- For loading existing database, endure the relevant CVS file is located in the same directory as main.py file.
- If files do not exist, the program will start with an empty list.
- Data is only saved when exitting the program. 