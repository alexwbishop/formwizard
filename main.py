# main.py
#  the entry point and should not be imported by other modules.

# Import necessary modules and functions
from user_choices import get_user_choice
from questionnaire import FormWizard

# Main function that orchestrates the form handling based on user input
def main(): 
    print("......System warming up......")
    print("Welcome to FormWizard!") 
    user_choice = get_user_choice()
    wizard = FormWizard(user_choice)
    wizard.run_session()
    print("Goodbye!")


# Entry point check to prevent code from executing when imported
if __name__ == "__main__":
    print("main.py initiated as main.")
    main()