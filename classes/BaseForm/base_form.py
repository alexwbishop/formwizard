# base_form.py

# BaseForm: This is the PARENT CLASS that contains common methods and attributes for all forms.
	#- Attributes: Common fields like entity name, signer name, etc.
	#- Methods: Data validation, PDF generation, etc.

# get current date & time to use in the timestamp feature
from datetime import datetime

# define commonly used form fields for all states (BaseForm)
class BaseForm:
    def __init__(self, **kwargs):
        # Form Metadata
        self.filing_type = kwargs.get('filing_type', None)
        self.jurisdiction = kwargs.get('jurisdiction', None)
        self.jurisdiction_instance = kwargs.get('jurisdiction_instance', None)
        self.residency = kwargs.get('residency', None)
        self.version_last_updated = kwargs.get('version_last_updated', datetime.now())
        self.attachments = kwargs.get('attachments', None)
        
        # Entity Information
        self.agent_city = kwargs.get('agent_city', None)
        self.agent_county = kwargs.get('agent_county', None)
        self.agent_name = kwargs.get('agent_name', None)
        # ... (other attributes)
        
        # Signature Block Info
        self.hard_copy_required = kwargs.get('hard_copy_required', None)
        # ... (other attributes)
        
        # Order-Specific Details
        self.line_number = kwargs.get('line_number', None)
        # ... (other attributes)
        
    def validate_data(self):
        pass
    # ... (other methods)

class DEForm(BaseForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.signed_on_day = kwargs.get('signed_on_day', None)
        self.signed_on_month = kwargs.get('signed_on_month', None)
        self.signed_on_year = kwargs.get('signed_on_year', None)
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



