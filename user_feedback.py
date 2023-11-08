# user_feedback.py

# Functions relating to asking for user experience feedback and logging it

# Import necessary modules and functions
from user_choices import get_user_choice
from form_wizard import FormWizard
import user_feedback

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
    user_feedback.init()  # Initialize the user feedback module
    main()
    user_feedback.main_feedback_flow()

# This module can then be called at the end of your main script

#In this setup, user_feedback.init() is called before main() to ensure that any necessary setup for the feedback module is done before 
# the main application logic starts. Then, after main() completes, user_feedback.main_feedback_flow() is called to collect and save the user feedback.
#Also, note that in user_feedback.py, the collect_feedback function should just return the collected feedback, and 
# the save_feedback function should take care of saving it. This separation of concerns makes your code cleaner and more maintainable.


