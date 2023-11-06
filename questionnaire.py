# questionnaire.py

# Initial Session Questions, Entity & Filing Selection
import pandas as pd
from enums.filing_type import FILING_TYPES, is_valid_new_name
from enums.filing_type import FilingType, FILING_QUESTIONS
from enums.residency import Residency
from enums.entity_types import EntityType
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from main import choice

# Define 'determine_residency' as a top-level function - because it drives the logic of other class-based functions
def determine_residency(domestic_state):
    # Example logic, this will depend on your specific business rules
    if domestic_state == 'DE':  # Assuming 'DE' for Delaware, as an example
        return Residency.DOMESTIC
    else:
        return Residency.FOREIGN

# Functions
def initiate_filing_questionnaire():
    print("Welcome to the Filing Questionnaire Session.")
    num_forms = ask_quantity_of_filings()  # This will return an integer
    return num_forms  # Return the number of forms as an integer

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

def get_manual_input_data():
    print("Please provide the following info: ")
    data = {}
    #data['Target'] = input("Enter target: ")
    #data['CT Order Number'] = input("Enter CT Order Number: ")
    data['Domestic State'] = input("Enter the domestic state: ")
    #data['Current Registered Agent'] = input("Enter current registered agent: ") # make this into a selection from a list
    #data['Current Status'] = input("Enter current status: ")
    #data['Registration Date'] = input("Enter registration date: ")
    data['Filing Type'] = input("Enter filing type: ")

    # Confirm agent name - # NEED TO TEST - JUST ADDED
    confirm_agent_name()
    # Collect Signer's Name
    get_signer_name()    # NEED TO TEST - JUST ADDED
    # Confirm Signer's Name
    confirm_signer() # NEED TO TEST - JUST ADDED
    # Initialize list to store form instances also went through and
    forms = []
    # Loop through the number of forms specified
    return data

def get_data():
    print("Welcome to the FormWizard Manual Info Entry Questionnaire!")
    entity_data = get_manual_input_data()

    # Ensure 'Domestic State' is set
    if 'Domestic State' not in entity_data or not entity_data['Domestic State']:
        entity_data['Domestic State'] = input("Domestic State was not obtained from import. Please provide the domestic state: ")

    # Now that entity_data is fully populated, determine the residency class
    entity_data['Residency Class'] = determine_residency(entity_data['Domestic State'])

    # entity data is loaded into the session, and the session is ready to begin the filing-specific question phase
    return entity_data

# define the core data collection and form assembly process (FormWizard)
class FormWizard:
    def run_session(self):
        print("Initializing FormWizard session...")
        # Collect the data for each entity from the user
        for _ in range(ask_quantity_of_filings()):
            entity_data = get_data(choice) # NOT DEFINED? Waze
            # Validate and store entity data
            valid, error_message = self.validate_data(entity_data)
            if not valid:
                self.handle_errors(error_message)
                continue  # Skip to the next entity if the current one is invalid
            self.entities_data.append(entity_data)
            # user could be given option to skip data entry of missing fields, then fill post-session manually,
            # but we would want to build in a reminder feature for that.
            
    def __init__(self):
        self.entities_data = []
        self.filing_data = []

    def validate_data(self, data):
        # Implement data validation here
        # For example: 
        # if not data['entity_name']:
        #     return False, "Entity name is missing."
        # ... and so on for other validations
        # validation of answers to questions specific to the filing type
        def handle_changeofagent():
        # e.g. for Change of Agent, if we needed prior Registered agent info, we would want to validate that it's not the same as current agent
        # info, however currently supported state and filing types (DE) does not need prior agent info
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

            # how to check if the new name is valid
        def handle_nameamendment(current_name: str):
            print(f"validating {current_name}...")
            # Ask for the new name
            new_name = input(FILING_QUESTIONS[FilingType.NAME_AMENDMENT][0])
            # Validate the new name
            while not is_valid_new_name(current_name, new_name):
                # Ask for the new name again if it's invalid
                new_name = input(FILING_QUESTIONS[FilingType.NAME_AMENDMENT][0])
            # Store the new name or process it as needed
            # DALIA #  DO I NEED TO PUT A return HERE for it to send the validation back to the main function?
            pass

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
        
        return True, ""
    

    # # Display the collected data to the user for review
    #     def display_data_for_confirmation(self):
    #         for entity in self.entities_data:
    #             print(entity)
    #         for filing in self.filing_data:
    #             print(filing)
    #         # Get user confirmation
    #         confirmation = input("Do you confirm the provided data? (Yes/No): ")
    #         if confirmation.lower() == 'yes':
    #             return True
    #         return False
    
   # Since you mentioned that the coordinates JSON files have moved, you'll need to update the paths to these files in your code once you integrate the PDF generation functionality.
    def generate_forms(self):
        print("Generating forms...")
        form_template_path = f"StateForms/{Jurisdiction}/{Jurisdiction}-{entity_type}-{residency}-{filing_type}.pdf"
        print("Loaded file: ", form_template_path)  
check_file_path(form_template_path)
# Function to get PDF dimensions
print("Getting PDF dimensions...")
get_pdf_dimensions(pdf_path)
# Function to populate form fields
print("Populating form fields for: ", entity_name) 
populate_form()
# Function to merge text PDF onto blank form
print("Merging responses onto blank form fields...")
merge_overlay_pdf()
# Create an instance of the Jurisdiction class
current_jurisdiction = Jurisdiction.create_jurisdiction(state_name_mapping[state], state)
de_jurisdiction = Jurisdiction.create_jurisdiction("Delaware", "DE")
ca_jurisdiction = Jurisdiction.create_jurisdiction("California", "CA")

# Create a single BaseForm instance with defaults
form_instance = BaseForm(
    domestic_state=DEFAULTS.get('domestic_state', 'DE'), 
    form_status=DEFAULTS.get('form_status', 'Blank'), 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)

# date & time validation - not used
#date_time_input = input("Enter date and time (format: YYYY-MM-DD HH:MM:SS): ")
#
#if validate_date_time(date_time_input):
#    print("Valid date and time!")
#else:
#    print("Invalid date and time format!")

# Overwrite form instance attributes as necessary
if some_condition:
    form_instance.domestic_state = "DE"

# Now that form_instance is defined, you can update de_jurisdiction with it if needed
de_jurisdiction.jurisdiction_instance = form_instance
 
def handle_errors(self, error):
    print(f"An error occurred: {error}")
    # Additional error handling can be implemented here

## END OF FORM GENERATION PROCESS ##

    def end_or_continue(self):
        choice = input("Would you like to end the session or continue with another task? (End/Continue): ")
        if choice.lower() == 'end':
            print("Thank you for using FormWizard!")
            return
        # If the user wants to continue, redirect them to the starting point or offer other options

        # entity data error validation
        valid, error_message = self.validate_data(self.entities_data)
        if not valid:
            self.handle_errors(error_message)
            return

        if not self.display_data_for_confirmation():
            # If the user doesn't confirm the data, give them a chance to modify it
            # ...
            return

        self.generate_forms()

# generate a PDF summary of the session - forms completed, any outstanding info, supplemental forms needed, etc.        
def generate_summary(self):
        # Path for the summary log or PDF
        path = "summary.pdf"  # Modify this as required
        
        # Create the PDF with the summary data
        c = canvas.Canvas(path, pagesize=letter)
        width, height = letter
        
        # Add title and other header info
        c.drawString(100, height - 100, "FormWizard Summary")
        
        # Loop through entities_data & filing_data and add to the PDF
        
        # Save the PDF
        c.save()

# record user feedback collection on the session - save to a dedicated log file
def collect_feedback(self):
        rating = input("On a scale of 1-10, how would you rate your experience with FormWizard? ")
        
        # Validate rating
        while not rating.isdigit() or not 1 <= int(rating) <= 10:
            rating = input("Please provide a valid rating between 1 and 10: ")
        
        comments = input("Any additional comments or suggestions? ")
        
        with open("feedback_log.txt", "a") as f:
            f.write(f"Rating: {rating}\nComments: {comments}\n\n")

# give user opportunity to exit or restart a new session
def end_or_continue(self):
        self.generate_summary()
        self.collect_feedback()
        
        choice = input("Would you like to end the session or continue with another task? (End/Continue): ")
        if choice.lower() == 'end':
            print("Thank you for using FormWizard! Have a great day.")
            return
        # If the user wants to continue, redirect them to the starting point or offer other options
        # IS THIS DEFINED YET? #
        # self.run_session()     ????

#Usage:
# To start the session:
#wizard = FormWizard()
#wizard.run_session()
# You can call initiate_filing_questionnaire() to start the process
# You can call get_data() to get the data for a single entity
if __name__ == "__main__":
    wizard = FormWizard()
    print("this is the test run of questionnaire.py")
    wizard.run_session()