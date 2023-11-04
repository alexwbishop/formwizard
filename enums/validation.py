# validation.py
#
# contains functions for validating DE-specific form data
from constants.name_restrictions import RESTRICTED_WORDS
from constants.entity_indicators import VALID_ENTITY_INDICATORS
from constants.name_restrictions import MAX_PURPOSE_LENGTH
from datetime import datetime

# validate address is in-state
def instate_address(address: str) -> bool:
    if "DE" not in address:
        print("Address must be in the state of Delaware.")
        return False
    # Other address validations can be added here
    return True

# used only if registered agent is an individual or non-CT entity.
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
def is_valid_entity_name(entity_name: str) -> bool:
    if not any(indicator in entity_name for indicator in VALID_ENTITY_INDICATORS):
        print("Entity name must include a valid entity indicator (e.g., LLC, Inc., Corp.).")
        return False
    for word in RESTRICTED_WORDS:
        if word in entity_name:
            print(f"'{word}' is a restricted word for entity names.")
            return False
    return True

# validates that formation date is a valid date
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
    
    
