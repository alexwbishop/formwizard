# signature_block.py
#
# contains parameters for signature block related fields
from enum import Enum, auto

# methods of document execution
class SignatureType(Enum):
    PDF_SCAN = auto()
    CONFORMED = auto()
    HARD_COPY = auto()
    NOTARIZED = auto()
    TYPE_IN = auto()
    E_SIGNATURE = auto()
    # ... add other signature types

# signer title matches with entity type
ENTITY_TITLE_MATCH = {
    'LLC': ['Manager', 'Member', 'Authorized Person'],
    'Corp': ['CEO', 'President', 'Treasurer', 'Vice President', "COO", "Chief Operating Officer", 
             "Chief Executive Officer", "Executive Vice President", "Chief Executive Officer",
             'Secretary', 'Director', 'Assistant Secretary', "CFO", "Chief Financial Officer", "Assistant Treasurer"],
    'LP': ['General Partner', 'Limited Partner'],
    'GP': ['General Partner'],
    'LLP': ['General Partner', 'Limited Partner'],
    'WITH_POA': ['Power of Attorney', 'Attorney in Fact', 'Authorized Person']
}
# validate signer title matches with entity type
def is_valid_signer_title(entity_type: str, title: str) -> bool:
    if title not in ENTITY_TITLE_MATCH.get(entity_type, []):
        print(f"'{title}' is not a valid title for {entity_type}.")
        return False
    return True

# validate signer name is an individual's name
def is_valid_signer_name(name: str) -> bool:
    if 1 < len(name.split()) <= 2:  # expecting a first and last name
        return True
    print("Signer name does not seem to be a valid individual's name.")
    return False

def get_signer_details(entity_type):
    signer_name = input("Please enter the signer's name: ")

    # Providing title options based on entity type
    if entity_type == 'Corporation':
        print("Select the title or write in your own:")
        print("1. President")
        print("2. Vice President")
        print("3. Secretary")
        print("4. Other (Write-in)")

        choice = input("Enter choice: ")
        if choice == '4':
            signer_title = input("Enter the custom title: ")
        else:
            titles = ["President", "Vice President", "Secretary"]
            signer_title = titles[int(choice)-1]

    elif entity_type == 'LLC':
        print("Select the title:")
        print("1. Manager")
        print("2. Member")
        print("3. Authorized Person")

        choice = input("Enter choice: ")
        titles = ["Manager", "Member", "Authorized Person"]
        signer_title = titles[int(choice)-1]

    return signer_name, signer_title

def handle_multiple_signers(entity_count, entity_type):
    same_signer = input("Is it the same signer for all forms? (yes/no) ")

    signers_list = []

    if same_signer.lower() == 'yes':
        signer_name, signer_title = get_signer_details(entity_type)
        signers_list.append((signer_name, signer_title))

    else:
        for i in range(entity_count):
            print(f"Enter details for signer of entity {i+1}")
            signer_name, signer_title = get_signer_details(entity_type)
            signers_list.append((signer_name, signer_title))

    return signers_list

from datetime import datetime, timedelta

def get_signature_date():
    apply_signature = input("Do you want to apply the conformed signature to the form? (yes/no) ")
    if apply_signature.lower() == 'yes':
        date_format = "%Y-%m-%d"
        today = datetime.today()

        while True:
            chosen_date = input(f"Please enter the desired signature date (format: {date_format}): ")
            chosen_datetime = datetime.strptime(chosen_date, date_format)

            if today <= chosen_datetime <= (today + timedelta(days=90)):
                return chosen_date
            else:
                print(f"Date should be between {today.strftime(date_format)} and {(today + timedelta(days=90)).strftime(date_format)}")
    else:
        return None

