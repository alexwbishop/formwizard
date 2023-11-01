# base_form.py

# BaseForm: This is the PARENT CLASS that contains common methods and attributes for all forms.
	#- Attributes: Common fields like entity name, signer name, etc.
	#- Methods: Data validation, PDF generation, etc.

# get current date & time to use in the timestamp feature
from datetime import datetime
from ..Jurisdiction.jurisdiction import Jurisdiction

# define common form fields
class BaseForm:
    def __init__(self, jurisdiction_instance, form_status=None, attachments=None, line_number=None, signer_midinit=None, order_number=None, entity_name=None, domestic_state=None, agent_name=None, agent_street1=None, agent_street2=None, agent_city=None, agent_state=None, agent_zip=None, agent_county=None, session_id=None, session_timestamp=None, signer_name=None, signer_first=None, signer_mid=None, signer_last=None, signer_title=None, signer_title_ext=None, sig_conformed=None, sig_typed=None, signed_on_date=None, state_id=None, business_purpose=None, phys_street1=None, phys_street2=None, phys_city=None, phys_state=None, phys_zip=None, phys_county=None, mail_street1=None, mail_street2=None, mail_city=None, mail_state=None, mail_zip=None, mail_county=None, domestic_street1=None, domestic_street2=None, domestic_city=None, domestic_zip=None, domestic_county=None, user_id=None):
        
        # entity name
        self.entity_name = entity_name

        # a reference to an instance of the 'Jurisdiction' class within each form object
        self.jurisdiction_instance = jurisdiction_instance 
        # This allows access to all the state-specific attributes and methods through that reference.
        
        # Create a DE instance of the Jurisdiction class
        de_jurisdiction = Jurisdiction("Delaware", "DE")

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

        # signer_first
        self.signer_first = signer_first

        # signer_mid
        self.signer_mid = signer_mid

        # signer_last
        self.signer_last = signer_last

        # signer_name (concatenated)
        self.signer_name = signer_name

        # signer_midinit ## make this dynamically the first initial of signer_mid
        self.signer_midinit = signer_midinit

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

        # domestic_street1
        self.domestic_street1 = domestic_street1

        # domestic_street2
        self.domestic_street2 = domestic_street2

        # domestic_city
        self.domestic_city = domestic_city

        # domestic_zip
        self.domestic_zip = domestic_zip

        # domestic_county
        self.domestic_county = domestic_county

        # user_ID
        self.user_id = user_id # user who completed the form (e.g. John.Smith) 

        # session_id 
        self.session_id = session_id #formWizard unique form-prep session ID#

        # session_timestamp 
        self.session_timestamp = session_timestamp # for when forms were filled out

        # form status
        self.form_status = form_status

        # date the form/template version was last updated
        self.last_updated_timestamp = "10.1.2023"
        # want to replace None above with datetime.now() as old forms are updated with new versions

        # attachments 
        self.attachments = [attachments] # List or dictionary to hold additional documents that need to be submitted with the form (e.g. eSignature page)
        
        # line_number
        self.line_number = line_number  # For internal order tracking
        
        # order_number
        self.order_number = order_number  # For internal order tracking

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



