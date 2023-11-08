# main.py
#  the entry point and should not be imported by other modules.

# Import necessary modules and functions
from form_wizard import FormWizard
from session_wizard import SessionWizard
from dispatch_wizard import DispatchWizard
from user_choices import get_data_input_method
import user_feedback
import excel_import
import data_preparation

# Listener function that triggers the next step based on user's choice of data input method
def data_input_method_listener(dispatch_wizard, session_wizard, choice):
    if choice == 'excel':
        # Trigger Excel import process
        excel_data = excel_import.import_data()
        session_wizard.store_entity_data(excel_data)
    elif choice == 'manual':
        # Trigger manual data input process
        manual_data = data_preparation.capture_data()
        session_wizard.store_entity_data(manual_data)
    
    # Dispatch an event to indicate that entity data is ready
    dispatch_wizard.dispatch('entity_data_ready')

# Main function that orchestrates the form handling based on user input
def main(): 
    # Initialize DispatchWizard and SessionWizard
    print("......System warming up......")
    print("loading SessionWizard...")
    session_wizard = SessionWizard()
    print("SessionWizard loaded.")
    print("loading DispatchWizard...")
    dispatch_wizard = DispatchWizard()
    print("DispatchWizard loaded.")
    print("loading Initial Questionnaire...")
    
    # Register event listeners
    dispatch_wizard.register('data_input_method_chosen', lambda choice: data_input_method_listener(dispatch_wizard, session_wizard, choice))

    # Start the application flow
    print("Welcome to FormWizard!")
    # Get the user's choice of data input method
    data_input_method = get_data_input_method()
    # Store the choice in the SessionWizard
    session_wizard.update_choices('data_input_method', data_input_method)
    dispatch_wizard.dispatch('data_input_method_chosen', data_input_method)
    # Later on, when you need to access this choice:
#data_input_method = session_wizard.choices.get('data_input_method')
#if data_input_method == 'excel':
    # Proceed with Excel import
#elif data_input_method == 'manual':
    # Proceed with manual data input

    # Process any queued events
    dispatch_wizard.process_events()

    # Wait for entity data to be ready before continuing
    dispatch_wizard.wait_for_event('entity_data_ready')
    
    # Continue with the FormWizard process
    form_wizard = FormWizard(session_wizard.get_entity_data())
    form_wizard.run_session()
    print("Goodbye!")

# Entry point check to prevent code from executing when imported
if __name__ == "__main__":
    # Initialize the user feedback module
    user_feedback.init()
    main()
    user_feedback.main_feedback_flow()