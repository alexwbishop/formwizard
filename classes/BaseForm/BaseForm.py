# BaseForm.py

# BaseForm: This is the PARENT CLASS that contains common methods and attributes for all forms.
	#- Attributes: Common fields like entity name, signer name, etc.
	#- Methods: Data validation, PDF generation, etc.
# using **kwargs to capture all the keyword arguments. 
# This is a common Python practice to handle numerous parameters, especially when they are mostly 
# optional. However, remember that using **kwargs can sometimes make it less clear what arguments 
# a class or function expects, so use it when you have a clear pattern for handling the incoming 
# values, as shown in the loop that sets the attributes.

# begin
from datetime import datetime

class BaseForm:
    """
    BaseForm class is the parent class for all forms.
    Attributes:
        entity_name: The name of the entity.
        entity_type: The type of entity (e.g., LLC, Corporation).
        residency: Residency status of the entity.
        ...
    """

    def __init__(self, jurisdiction_instance, **kwargs):
        self.jurisdiction_instance = jurisdiction_instance 
        self.last_updated_timestamp = datetime.now()  # Set current time when object is created
        
        # All other attributes with None as default, set via keyword arguments
        attributes = [
            'residency', 'filing_type', 'entity_type', 'jurisdiction', 'form_status',
            'attachments', 'line_number', 'signer_midinit', 'order_number', 'entity_name',
            'domestic_state', 'agent_name', 'agent_street1', 'agent_street2', 'agent_city',
            'agent_state', 'agent_zip', 'agent_county', 'session_id', 'session_timestamp',
            'signer_name', 'signer_first', 'signer_mid', 'signer_last', 'signer_title',
            'signer_title_ext', 'sig_conformed', 'sig_typed', 'signed_on_date', 'state_id',
            'business_purpose', 'phys_street1', 'phys_street2', 'phys_city', 'phys_state',
            'phys_zip', 'phys_county', 'mail_street1', 'mail_street2', 'mail_city', 
            'mail_state', 'mail_zip', 'mail_county', 'domestic_street1', 'domestic_street2',
            'domestic_city', 'domestic_zip', 'domestic_county', 'user_id'
        ]
        
        # Initialize all attributes, allowing for easy extension or modification
        for attribute in attributes:
            setattr(self, attribute, kwargs.get(attribute))
        
        self.attachments = kwargs.get('attachments', [])  # Initialize as empty list if not provided

    # You may want to include @property decorators for computed attributes
    @property
    def signer_name(self):
        # Assuming signer_first, signer_midinit, and signer_last are already set
        mid_initial = f" {self.signer_midinit}." if self.signer_midinit else ""
        return f"{self.signer_first}{mid_initial} {self.signer_last}"

    @signer_name.setter
    def signer_name(self, value):
        names = value.split()
        self.signer_first = names[0]
        self.signer_last = names[-1]
        if len(names) > 2:
            self.signer_midinit = names[1][0]  # Assumes the middle initial is the first character of the second name
        
    def validate_data(self):
        # Placeholder for data validation logic
        pass

    def generate_pdf(self):
        # Placeholder for PDF generation logic
        pass

    def save_draft(self):
        # Placeholder for save draft logic
        pass

    def load_draft(self):
        # Placeholder for load draft logic
        pass