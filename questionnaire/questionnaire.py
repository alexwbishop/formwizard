# questionnaire.py

# Initial Session Questions, Entity & Filing Selection
from excel_import import load_data_from_excel, get_entity_data
import pandas as pd
from enums.filing_type import FILING_TYPES, is_valid_new_name
from enums.filing_type import FilingType
from enums.residency import Residency
from enums.entity_types import EntityType
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Functions
def initiate_filing_questionnaire():
    print("Welcome to the Filing Questionnaire Session.")
    num_forms = ask_quantity_of_filings()
    entity_names = ask_entity_names(num_forms)
    # Continue with additional questions or processing
    return entity_names

# asks for number of forms to fill out in current session
def ask_quantity_of_filings() -> int:
    while True:
        try:
            num_forms = int(input("How many forms do you want to fill out today? (max 10): "))
            if 1 <= num_forms <= 10:
                return num_forms
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.") 


# offer excel import option before manual data entry
def get_data_source_choice():
    choice = input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
    while choice not in ['excel', 'manual']:
        print("Invalid choice. Please choose 'excel' or 'manual'.")
        choice = input("Would you like to import data from an Excel sheet or input manually? ")
    return choice

def get_data(choice):
    if choice == 'excel':
        filename = input("Please provide the Excel filename: ")
        df = load_data_from_excel(filename)
        entity_name = input("Enter the entity name: ")
        entity_data = get_entity_data(df, entity_name)
        
        # Validate the data and ask for any missing info
        for key, value in entity_data.items():
            if not value or pd.isnull(value):
                entity_data[key] = input(f"Please provide the {key}: ")

    elif choice == 'manual':
        # Here, you can use the existing code you've written to get input for each data field
        entity_data = get_manual_input_data()

    return entity_data

def get_manual_input_data():
    data = {}
    data['Target'] = input("Enter target: ")
    data['CT Order Number'] = input("Enter CT Order Number: ")
    data['Domestic State'] = input("Enter the domestic state: ")
    data['Current Registered Agent'] = input("Enter current registered agent: ")
    data['Current Status'] = input("Enter current status: ")
    data['Registration Date'] = input("Enter registration date: ")
    data['Filing Type'] = input("Enter filing type: ")

    return data


def ask_entity_names(num_forms: int) -> list:
    entity_names = []
    for i in range(num_forms):
        while True:
            entity_name = input(f"Enter entity name for form {i+1}: ").strip()
            # Add your validation logic here if needed
            if validate_entity_name(entity_name, entity_names):
                entity_names.append(entity_name)
                break
            else:
                print("Invalid or duplicate entity name. Please try again.")
    return entity_names

def validate_entity_name(entity_name: str, existing_names: list) -> bool:
    # Add your entity name validation logic here
    if entity_name in existing_names:
        return False
    # Add more rules as needed
    return True

# You can call initiate_filing_questionnaire() to start the process
if __name__ == "__main__":
    initiate_filing_questionnaire()

# defines main script function - can import from excel then, ask for missing data via manual input
def main():
    choice = get_data_source_choice()
    entity_data = get_data(choice)
    # Continue with the rest of your script

# main script function begins here    
main()



# RETURN ENTITY DATA FROM EXCEL HERE? #
# VALIDATE ENTITY DATA? #


# Somewhere in your code, you would determine the entity's domestic state
domestic_state = Residency.domestic_state  # This would be determined dynamically based on user input or data import
entity_name = ?EXCELIMPORT?.entity_name # This would be determined dynamically based on user input or data import


# define filing types available for selected residency/entity type combination (i.e. Domestic LLC)
def available_filings(domestic_state, filing_state=Residency.DELAWARE):
    if domestic_state == filing_state:
        # Exclude 'FORMATION' for domestic entities, as they already exist in the state
        return [filing for filing in FilingType if filing != FilingType.FORMATION]
    else:
        # Return all filing types for foreign entities
        return list(FilingType)

# begin selecting filings for the entities selected
def select_filing_types(entity_count):
    selected_filings = {}

    for i in range(entity_count):
        print(f"\nSelect filing type for entity {i+1}:")
        for idx, filing in enumerate(FILING_TYPES, 1):
            print(f"{idx}. {filing}")

        while True:
            try:
                choice = int(input("Enter choice: "))
                if 1 <= choice <= len(FILING_TYPES):
                    selected_filings[f"Entity {i+1}"] = FILING_TYPES[choice-1]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")


    # Then you call available_filings with the entity's domestic state
    selected_filings = available_filings(domestic_state)
    return selected_filings

# display confirmation to user question, review, ask for confirmation, if not go back and change selections
print("Confirmation: " selected_filings) #E X P A N D

# ONCE CONFIRMED, BEGIN FILING-SPECIFIC QUESTIONS
def get_questions_for_filing(filing_type: FilingType) -> list:
    return FILING_QUESTIONS.get(filing_type, [])


# validation of answers to questions for each filing type
def handle_changeofagent():
    pass
    
def handle_incorporation():
    pass

def handle_registration():
    pass

def handle_qualification():
    pass

def handle_withdrawal():
    pass

def handle_cancellation():
    pass

def handle_reinstatement():
    pass

def handle_nameamendment(current_name: str):
    new_name = input(FILING_QUESTIONS[FilingType.AMENDMENT][0])
    while not is_valid_new_name(current_name, new_name):
        new_name = input(FILING_QUESTIONS[FilingType.AMENDMENT][0])

def handle_stockamendment():
    pass

def handle_annualreport():
    pass

def handle_addressupdate():
    pass

def handle_officialsupdate():
    pass

def handle_merger():
    pass

def handle_conversion():
    pass

def handle_dissolution():
    pass

def handle_correction():
    pass

def handle_businesslicense():
    pass

def handle_miscfiling():
    pass

# review answers to all questions after validation, print to user, ask for confirmation, if not go back and change selections
class FormWizard:

    def __init__(self):
        self.entities_data = []
        self.filing_data = []

    def validate_data(self, data):
        # Implement data validation here
        # For example: 
        # if not data['entity_name']:
        #     return False, "Entity name is missing."
        # ... and so on for other validations
        return True, ""

    def display_data_for_confirmation(self):
        # Display the collected data to the user for review
        for entity in self.entities_data:
            print(entity)
        for filing in self.filing_data:
            print(filing)
        
        # Get user confirmation
        confirmation = input("Do you confirm the provided data? (Yes/No): ")
        if confirmation.lower() == 'yes':
            return True
        return False

    def generate_forms(self):
        # Use the collected and validated data to generate the forms
        # This could involve interacting with predefined templates or other mechanisms
        pass

    def handle_errors(self, error):
        print(f"An error occurred: {error}")
        # Additional error handling can be implemented here

    def end_or_continue(self):
        choice = input("Would you like to end the session or continue with another task? (End/Continue): ")
        if choice.lower() == 'end':
            print("Thank you for using FormWizard!")
            return
        # If the user wants to continue, redirect them to the starting point or offer other options

    def run_session(self):
        # Collect the data from the user or from an Excel sheet
        # ...

        valid, error_message = self.validate_data(self.entities_data)
        if not valid:
            self.handle_errors(error_message)
            return

        if not self.display_data_for_confirmation():
            # If the user doesn't confirm the data, give them a chance to modify it
            # ...
            return

        self.generate_forms()

def generate_summary(self):
        # Path for the summary log or PDF
        path = "summary.pdf"  # Modify this as required
        
        # Create the PDF with the summary data
        c = canvas.Canvas(path, pagesize=letter)
        width, height = letter
        
        # Add title and other header info
        c.drawString(100, height - 100, "FormWizard Summary")
        
        # Loop through entities_data & filing_data and add to the PDF
        # ...
        
        # Save the PDF
        c.save()

def collect_feedback(self):
        rating = input("On a scale of 1-10, how would you rate your experience with FormWizard? ")
        
        # Validate rating
        while not rating.isdigit() or not 1 <= int(rating) <= 10:
            rating = input("Please provide a valid rating between 1 and 10: ")
        
        comments = input("Any additional comments or suggestions? ")
        
        with open("feedback_log.txt", "a") as f:
            f.write(f"Rating: {rating}\nComments: {comments}\n\n")

def end_or_continue(self):
        self.generate_summary()
        self.collect_feedback()
        
        choice = input("Would you like to end the session or continue with another task? (End/Continue): ")
        if choice.lower() == 'end':
            print("Thank you for using FormWizard!")
            return
        # If the user wants to continue, redirect them to the starting point or offer other options


# To start the session:
wizard = FormWizard()
wizard.run_session()

#
