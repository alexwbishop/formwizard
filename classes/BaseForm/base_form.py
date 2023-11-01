# base_form.py

# BaseForm: This is the PARENT CLASS that contains common methods and attributes for all forms.
	#- Attributes: Common fields like entity name, signer name, etc.
	#- Methods: Data validation, PDF generation, etc.

# get current date & time to use in the timestamp feature
from datetime import datetime

# define BaseForm common data fields (e.g. fields generally needed for at least 1 form within all 51 jurisdictions)
class BaseForm:
	def __init__(self, **kwargs):
        # Common Form Metadata
        self.filing_type = kwargs.get('filing_type', 'Change of Agent')
        self.jurisdiction = kwargs.get('jurisdiction', 'DE')
        self.jurisdiction_instance = kwargs.get('jurisdiction_instance', None)
        self.residency = kwargs.get('residency', 'Foreign')
        self.version_last_updated = kwargs.get('version_last_updated', datetime.now())
        self.attachments = kwargs.get('attachments', None)
        
        # Registered Agent Information
	self.agent_name = kwargs.get('agent_name', 'C T Corporation System')
	self.agent_street1 = kwargs.get('agent_street1', None)
        self.agent_street2 = kwargs.get('agent_street2', None)
        self.agent_city = kwargs.get('agent_city', None)
	self.agent_state = kwargs.get('agent_state', None)
	self.agent_zip = kwargs.get('agent_zip', None)
        self.agent_county = kwargs.get('agent_county', None)
        
        # Entity-Specific Information
	self.state_id = kwargs.get('state_id', None)
	self.entity_type = kwargs.get('entity_type', 'LLC')
	self.domestic_state = kwargs.get('domestic_state', 'DE')
	self.entity_name = kwargs.get('entity_name', None)
	self.domestic_entity_name = kwargs.get('domestic_entity_name', None)
	self.forced_fict_name = kwargs.get('forced_fict_name', None)
	self.state_id = kwargs.get('state_id', None)
	self.formation_date = kwargs.get('formation_date', None)
	self.registration_date = kwargs.get('registration_date', None)
	# ... (other attributes)
        
        # Signature Block Info
        self.hard_copy_required = kwargs.get('hard_copy_required', 'No')
	self.signature_needed = kwargs.get('signature_needed', 'Yes')
	self.signature_type_allowed = kwargs.get('signature_type_allowed', 'E-Signature')
	self.signer_must_be_on_record = kwargs.get('signer_must_be_on_record', 'No')
	self.signer_name = kwargs.get('signer_name', None)
	self.signer_title = kwargs.get('signer_title', 'Authorized Person')
	self.signer_title_ext = kwargs.get('signer_title_ext', None)
	self.signer_titles_restricted = kwargs.get('signer_titles_restricted', 'No')
	self.signature_conformed = kwargs.get('signature_conformed', f"/s/ {self.signer_name}")
	self.signature_typed = kwargs.get('signer_name', None)
	self.poa_allowed = kwargs.get('poa_allowed', 'Yes')
	self.signed_on_date = kwargs.get('signed_on_date', datetime.now())
        # ... (other attributes)
        
        # Order-Specific Details
        self.line_number = kwargs.get('line_number', None)
	self.order_number = kwargs.get('order_number', None)
	self.target_number = kwargs.get('target_number', '1')
	self.supporting_docs_needed = kwargs.get('supporting_docs_needed', None)
	self.utilizing_poa = kwargs.get('utilizing_poa', 'Yes')
	self.form_status = kwargs.get('form_status', 'Blank')
	self.user_id = kwargs.get('user_id', 'alexander.bishop')
	self.user_email = f"{self.user_id}@wolterskluwer.com"
        # ... (other attributes)
        
	def validate_data(self):
        pass
    	# ... (other methods)

class DEForm(BaseForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        current_date = datetime.now()
        day = current_date.day
        if 10 <= day % 100 <= 20:
            day_str = str(day) + "th"
        else:
            day_str = str(day) + {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        self.signed_on_day = kwargs.get('signed_on_day', day_str) # Day spelled out e.g. 4th
        self.signed_on_month = kwargs.get('signed_on_month', current_date.strftime('%B'))  # Full month name
        self.signed_on_year = kwargs.get('signed_on_year', current_date.year)
        # ... (other DE-specific attributes)
        
    # DE-specific methods
    def special_DE_validation(self):
        pass
    # ... (other methods)

class DECorpForm(DEForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ... (Corp-specific attributes)
        
    # Corp-specific methods
    def special_corp_validation(self):
        pass
    # ... (other methods)

class CAForm(BaseForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
	    
        # ... (CA-specific attributes)
        
    # CA-specific methods
    def special_CA_validation(self):
        pass
    # ... (other methods)

# Example usage
# de_form = DEForm(filing_type="ChangeOfAgent", jurisdiction="DE", agent_city="Dover")



