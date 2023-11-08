# user_choices.py
#




# Function to ask the user to choose the data input method (Excel or Manual)
def get_user_choice():
    choice = input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
    while choice not in ['excel', 'manual']:
        print("Invalid choice. Please choose 'excel' or 'manual'.")
        choice = input("Would you like to import data from an Excel sheet or input manually? ")
    return choice