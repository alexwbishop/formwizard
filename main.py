# main.py

# Import necessary modules and functions
import user_input

# Main function that orchestrates the form handling based on user input
def main(): 
    print("......System warming up......")  # FIRST MESSAGE
    print("Welcome to FormWizard!") 
    print("We will now ask how you would like to input your data.")
    
    # Function to ask the user to choose the data input method (Excel or Manual)
    entity_data = user_input.get_data_source()
    print("Data source selected: " + entity_data)
# Entry point check to prevent code from executing when imported
if __name__ == "__main__":
    print("main.py initiated as main.")
    main()