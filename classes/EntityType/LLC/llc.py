# llc.py

# inherits from BaseForm.
# (this subclass is inheriting from BaseForm. This means that it will have access to all the attributes and methods defined in BaseForm)

from BaseForm import BaseForm

class LLC(BaseForm):
    def __init__(self, entity_name, jurisdiction_instance, user_id, **kwargs):
        super().__init__(entity_name, jurisdiction_instance, user_id, **kwargs)
        
        # Additional attributes specific to LLC
        self.domestic_state = kwargs.get('domestic_state', None)
        self.agent_name = kwargs.get('agent_name', None)
        self.agent_street1 = kwargs.get('agent_street1', None)
        self.agent_street2 = kwargs.get('agent_street2', None)
        self.agent_city = kwargs.get('agent_city', None)
        self.agent_state = kwargs.get('agent_state', None)
        self.agent_zip = kwargs.get('agent_zip', None)
        self.agent_county = kwargs.get('agent_county', None)
        self.signer_name = kwargs.get('signer_name', None)
        self.signer_title = kwargs.get('signer_title', None)
        self.signer_title_ext = kwargs.get('signer_title_ext', None)
        self.sig_conformed = kwargs.get('sig_conformed', None)
        self.sig_typed = kwargs.get('sig_typed', None)
        self.signed_on_date = kwargs.get('signed_on_date', None)
        self.state_id = kwargs.get('state_id', None)
        self.business_purpose = kwargs.get('business_purpose', None)
        self.phys_street1 = kwargs.get('phys_street1', None)
        self.phys_street2 = kwargs.get('phys_street2', None)
        self.phys_city = kwargs.get('phys_city', None)
        self.phys_state = kwargs.get('phys_state', None)
        self.phys_zip = kwargs.get('phys_zip', None)
        self.phys_county = kwargs.get('phys_county', None)
        self.mail_street1 = kwargs.get('mail_street1', None)
        self.mail_street2 = kwargs.get('mail_street2', None)
        self.mail_city = kwargs.get('mail_city', None)
        self.mail_state = kwargs.get('mail_state', None)
        self.mail_zip = kwargs.get('mail_zip', None)
        self.mail_county = kwargs.get('mail_county', None)
        self.instate_street1 = kwargs.get('instate_street1', None)
        self.instate_street2 = kwargs.get('instate_street2', None)
        self.instate_city = kwargs.get('instate_city', None)
        self.instate_state = kwargs.get('instate_state', None)
        self.instate_zip = kwargs.get('instate_zip', None)
        self.instate_county = kwargs.get('instate_county', None)