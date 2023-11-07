# auth.py
# User login and password authentication

# Imports
import re

# validates WK login username is correct format
# The regex used seems appropriate for the specified format. 
# The use of re.match checks for a match only at the beginning of the string.
def is_valid_username(username: str) -> bool:
    pattern = r"^[a-zA-Z]+\.[a-zA-Z]+$"
    return bool(re.match(pattern, username))

# placeholder and should eventually be replaced with a secure password input method.
#  Python's getpass library can hide the input for security purposes.
def get_password():
    password = input("Enter password: ")
    return password

# simulates the login process. In production, it would need to interface with an authentication 
# system, and passwords should never be compared as plain text. You would typically hash the input 
# password and compare it against a hashed password in a secure database.
def login():
    username = input("Enter username (format: firstname.lastname): ")
    if not is_valid_username(username):
        print("Invalid username format. Please use 'firstname.lastname'.")
        return False

    password = get_password()
    # Here you would typically check the username and password against a database or a stored value.
    # For placeholder purposes, we'll just check against a hardcoded value.
    hardcoded_password = "placeholderPassword"
    if password == hardcoded_password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False