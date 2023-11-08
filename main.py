# main.py

# Import necessary modules and functions
from enums.residency import determine_residency
from excel_import import import_from_excel
import user_input

def get_user_choice(choice):
    input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
        # Loop to ensure a valid response is entered
    while choice not in ['excel', 'manual']:
        print("Invalid choice. Please choose 'excel' or 'manual'.")
        choice = input("Would you like to import data from an Excel sheet or input manually? ")

def get_data_source():
        from questionnaire import initiate_filing_questionnaire
        from data_preparation import get_data
        # Prompt user for data import method, store the response in 'choice'
        get_user_choice()
        # Return the user's choice to the calling function OK
        if get_user_choice == 'excel':
        # Handle the Excel input method
            import_from_excel()
        elif get_user_choice == 'manual':
        # Handle the manual input method
            print("You have chosen to input data manually.")
            # Launch the questionnaire to determine the number of forms to process
            print("Booting up filing questionnaire. Please wait...")
            num_forms = initiate_filing_questionnaire() 
            # Loop to process each form as per the number specified
            for _ in range(num_forms):
            # Gather data manually for each form
                entity_data = get_data()
            # Determine and assign residency status based on the domestic state provided
            print("Determining residency based on data provided...")
            domestic_state = entity_data['Domestic State']
            entity_data['Residency'] = determine_residency(domestic_state)
            print("Residency determined successfully: " + entity_data['Residency'])
            # Additional steps to process each manually entered 'entity_data' can be done here
        else:
        # Handle other cases or raise an error
            print("Invalid choice. Please choose 'excel' or 'manual'.")
        return get_user_choice

# Main function that orchestrates the form handling based on user input
def main(): 
    print("......System warming up......")  # FIRST MESSAGE
    print("Welcome to FormWizard!") 
    print("We will now ask how you would like to input your data.")
    # Function to ask the user to choose the data input method (Excel or Manual)
    entity_data = get_data_source()
    print("Data source selected: " + entity_data)
# Entry point check to prevent code from executing when imported
if __name__ == "__main__":
    print("main.py initiated as main.")
    main()