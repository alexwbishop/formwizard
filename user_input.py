# user_input.py
#
# Functions relating to receiving and validating user input 

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

# 
def get_manual_input_data():
    print("Please provide the following info: ")
    data = {}
    data['Entity Name'] = input("Enter Entity Name: ")
    data['Domestic State'] = input("Enter the domestic state: ")
    #data['Current Registered Agent'] = input("Enter current registered agent: ") # make this into a selection from a list
    #data['Current Agent Address'] = input("Enter current agent's address: ") # make this into a selection from a list



#Where are these functions defined? 
# Prompt for agent name - # NEED TO TEST - JUST ADDED
# asks user for manual input of registered agent name (current or changing to)
confirm_agent_name()
    # Collect Signer's Name
get_signer_name()    # NEED TO TEST - JUST ADDED
    # Confirm Signer's Name
confirm_signer() # NEED TO TEST - JUST ADDED
