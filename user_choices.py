# user_choices.py
# This module contains the functions that handle user choices.

def get_data_input_method(dispatch_wizard, session_wizard):
    # Prompt the user to choose the data input method (Excel or Manual)
    print("Please choose your entity data input method:")
    print("1: Import entity data from an Excel sheet (i.e. audit)")
    print("2: Input data manually using the text-based interface")
    selection = input("Enter your choice (1 or 2): ")

    while selection not in ['1', '2']:
        print("Invalid choice. Please enter '1' for Excel or '2' for manual input.")
        selection = input("Enter your choice (1 or 2): ")

    # Convert the selection to a meaningful value
    data_method = 'excel' if selection == '1' else 'manual'

    # Update the session data with the user's choice
    session_wizard.update_choices('data_input_method', data_method)

    # Dispatch an event to indicate the user has made a choice
    dispatch_wizard.dispatch('data_input_method_chosen', data_method)

    return data_method