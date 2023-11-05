# validation.py
#
# contains functions for validating DE-specific form data
#
# Dalia's tips: 
#Error Handling: Add try-except blocks where appropriate to handle unexpected input.
#Case Sensitivity: Functions like is_valid_entity_name and is_valid_purpose should ideally handle words in a case-insensitive manner.
#Modularity: Consider breaking down some functions further if they start to handle too complex logic.
import re
from constants.name_restrictions import RESTRICTED_WORDS
from constants.entity_indicators import VALID_ENTITY_INDICATORS
from constants.name_restrictions import MAX_PURPOSE_LENGTH
from datetime import datetime

## checks if the address is within Delaware (DE).
# However, the check might be too simple since it only verifies the presence of "DE" in the string.
#  It may return false positives if "DE" is part of a street name or city name that is not actually 
# in Delaware. Consider using a more precise method such as regex or a specialized library for
#  address validation.
def instate_address(address: str) -> bool:
    if "DE" not in address:
        print("Address must be in the state of Delaware.")
        return False
    # Other address validations can be added here
    return True
## applied only if registered agent is an individual or non-CT entity (this is rare)
# consider edge cases where a valid individual's name might have more than two components, 
# such as those including a middle name, hyphenated last name, or titles.
def is_valid_agent_name(agent_name: str) -> bool:
    words = agent_name.split()
    # If there's more than one word but less than three, we assume it's a person's name
    if 1 < len(words) <= 2:
        return True
    # Otherwise, we check for business entity indicators
    elif any(indicator in agent_name for indicator in VALID_ENTITY_INDICATORS):
        return True
    else:
        print("Agent name does not seem to be a valid individual or business entity name.")
        return False
    
# validates that business purpose is not too long and does not contain restricted words
# checks for the length of the purpose and restricted words. It’s thorough in its current form. 
# Make sure that RESTRICTED_WORDS is comprehensive and up to date.
def is_valid_purpose(purpose: str) -> bool:
    if len(purpose) > MAX_PURPOSE_LENGTH:
        print("Business purpose is too long.")
        return False
    for word in RESTRICTED_WORDS:
        if word in purpose:
            print(f"'{word}' is a restricted word for business purpose.")
            return False
    return True

# validates that entity name contains a valid entity indicator and does not contain restricted words
# checks for the presence of valid entity indicators and restricted words, which is great. 
# Consider implementing case-insensitive checks to enhance robustness. 
# Right now, it might miss a word if it's capitalized differently.
def is_valid_entity_name(entity_name: str) -> bool:
    if not any(indicator in entity_name for indicator in VALID_ENTITY_INDICATORS):
        print("Entity name must include a valid entity indicator (e.g., LLC, Inc., Corp.).")
        return False
    for word in RESTRICTED_WORDS:
        if word in entity_name:
            print(f"'{word}' is a restricted word for entity names.")
            return False
    return True

# validates that formation date is a valid date using Python's datetime library for date validation.
def is_valid_formation_date(date_str: str) -> bool:
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # assuming date format as 'YYYY-MM-DD'
        if datetime(1900, 1, 1) <= date_obj <= datetime.today():
            return True
        print("Invalid date. Please provide a date between 1900 and today.")
        return False
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        return False

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
    