# session_wizard.py
# This module should be imported by other modules that need to store and retrieve session data.

class SessionWizard:
    def __init__(self):
        self.user_data = {}
        self.session_data = {}
        self.choices = {}

    def store_entity_data(self, data):
        self.update_session_data('entity_data', data)

    def get_entity_data(self):
        return self.session_data.get('entity_data')

    def update_user_data(self, key, value):
        self.user_data[key] = value

    def update_session_data(self, key, value):
        self.session_data[key] = value

    def update_choices(self, key, value):
        self.choices[key] = value

    def get_choice(self, key):
        return self.choices.get(key)

    # Add other methods to manipulate session data as needed
# SessionWizard now includes methods for storing and retrieving entity data, 
# which is a common operation in your application. 
# It also includes a method to retrieve user choices, 
# which can be used to determine the flow of the application based on user input.