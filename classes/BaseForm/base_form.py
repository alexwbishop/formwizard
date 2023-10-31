# base_form.py

# BaseForm: This is the PARENT CLASS that contains common methods and attributes for all forms.
	#- Attributes: Common fields like entity name, signer name, etc.
	#- Methods: Data validation, PDF generation, etc.

# get current date & time to use in the timestamp feature
from datetime import datetime

# define common form fields
class BaseForm:
    def __init__(self, entity_name, jurisdiction_instance, domestic_state, agent_name, agent_street1, agent_street2, agent_city, agent_state, agent_zip, agent_county, signer_name, signer_title, signer_title_ext, sig_conformed, sig_typed, signed_on_date, state_id, business_purpose, phys_street1, phys_street2, phys_city, phys_state, phys_zip, phys_county, mail_street1, mail_street2, mail_city, mail_state, mail_zip, mail_county, instate_street1, instate_street2, instate_city, instate_state, instate_zip, instate_county, user_id):
        # entity name
        self.entity_name = entity_name

        # (the below is a reference to an instance of the 'Jurisdiction' class within each form object.
        self.jurisdiction_instance = jurisdiction_instance 
            # This way, you can access all the state-specific attributes and methods through that reference.)
            
        # domestic state
        self.domestic_state = domestic_state   

        # agent_name
        self.agent_name = agent_name

        # agent_street1
        self.agent_street1 = agent_street1

        # agent_street2
        self.agent_street2 = agent_street2

        # agent_city
        self.agent_city = agent_city

        # agent_state
        self.agent_state = agent_state

        # agent_zip
        self.agent_zip = agent_zip

        # agent_county
        self.agent_county = agent_county

        # signer_name
        self.signer_name = signer_name

        # signer_title
        self.signer_title = signer_title

        # signer_title_ext
        self.signer_title_ext = signer_title_ext

        # sig_conformed
        self.sig_conformed = sig_conformed

        # sig_typed
        self.sig_typed = sig_typed

        # signed_on_date
        self.signed_on_date = signed_on_date

        # state_id
        self.state_id = state_id

        # business_purpose
        self.business_purpose = business_purpose

        # phys_street1
        self.phys_street1 = phys_street1

        # phys_street2
        self.phys_street2 = phys_street2

        # phys_city
        self.phys_city = phys_city

        # phys_state
        self.phys_state = phys_state

        # phys_zip
        self.phys_zip = phys_zip

        # phys_county
        self.phys_county = phys_county

        # mail_street1
        self.mail_street1 = mail_street1

        # mail_street2
        self.mail_street2 = mail_street2

        # mail_city
        self.mail_city = mail_city

        # mail_state
        self.mail_state = mail_state

        # mail_zip
        self.mail_zip = mail_zip

        # mail_county
        self.mail_county = mail_county

        # instate_street1
        self.instate_street1 = instate_street1

        # instate_street2
        self.instate_street2 = instate_street2

        # instate_city
        self.instate_city = instate_city

        # instate_state
        self.instate_state = instate_state

        # instate_zip
        self.instate_zip = instate_zip

        # instate_county
        self.instate_county = instate_county

    # + what else???
    #   self.what_else = what_else  

    # user ID whom completed the form (e.g. John.Smith) 
        self.user_id = user_id
    # form status
        self.form_status = None
    # date the form/template version was last updated
        self.last_updated_timestamp = None
        # may want to replace None above with datetime.now() when more forms are added
    # date 
        self.attachments = []  # List or dictionary to hold additional documents that need to be submitted with the form (e.g. eSignature page)
    # date
        self.line_number = None  # For internal order tracking
    # date
        self.order_number = None  # For internal order tracking

    def validate_data(self):
        # Implement your data validation logic here
        pass

    def generate_pdf(self):
        # Implement your PDF generation logic here
        pass

    def save_draft(self):
        # To save the current state of the form as a draft.
        pass

    def load_draft(self):
        #To load a saved draft of the form.
        pass



