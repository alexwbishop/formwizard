# jurisdiction.py
#- Jurisdiction: Subclasses for each jurisdiction (e.g., US states, DC, Local jurisdictions)
	#- Attributes: Fields specific to the jurisdiction.
	#- Methods: Logic specific to the jurisdiction.

#Inherits from FilingType - need to import/define FilingType
# # DALIA'S TIPS:
'''
Redundant Instance of FormUtility:
The FormUtility instance is created both in the BaseForm and Jurisdiction classes. Unless there's a specific need for each jurisdiction to have its own utility instance, you could just use the instance from BaseForm. This is especially relevant if FormUtility methods are stateless.

Duplicate Methods:
The some_method seems to be duplicated outside the Jurisdiction class scope, which would cause a syntax error. Make sure that methods are defined within the class body.

Inheritance Clarity:
It's not clear why Jurisdiction inherits from FilingType if FilingType isn't provided. The hierarchy should be logical: if Jurisdiction is a type of FilingType, the inheritance makes sense. Otherwise, reconsider the relationship.

Use of super().__init__:
The super().__init__ call appears to be passing a jurisdiction_instance, which implies that FilingType (and, by extension, BaseForm) expects such a parameter. Ensure that the parent class’s __init__ is designed to receive this.

Class Method Utility:
The create_jurisdiction class method is a factory method to create Jurisdiction objects, but currently, it only allows setting the name and abbreviation attributes. If you have defaults for other attributes or need to process input data before creating an instance, this method is useful. Otherwise, it might be redundant, as you can create instances directly.

Subclasses:
The subclasses for each state are empty and inherit everything from Jurisdiction without modification. If this is the intended behavior, then it's fine as placeholders. However, if each state has unique rules, these should be encoded into the respective subclasses.

Comments and Documentation:
Comments should be updated to reflect the current code. Any placeholder like # ... (rest of your code for subclasses) should either be filled with actual code or removed.

Code Consistency:
Ensure that naming conventions are consistent (e.g., Jurisdiction vs. FilingType and other classes). Consistent naming makes code more readable and maintainable.

Exception Handling:
Consider adding error handling for cases where invalid data might be passed to __init__.

Dynamic Last Updated Timestamp:
The last_updated_timestamp attribute should not be hard-coded. Instead, it should be dynamically generated based on when the form or template is updated. If it’s meant to be static, consider moving it to a class variable rather than an instance variable, assuming it’s shared across instances.
'''

from questionnaire import Filing_Type # DALIA HELP # - does this look right??

class Jurisdiction(Filing_Type):
    def __init__(self, name, abbreviation, signature_type_allowed=None, hard_copy_required=None, poa_allowed=None, tax_clearance_req=None, annual_reports_must_be_current=None, signer_must_be_on_record=None, signer_titles_restricted=None, jurisdiction_instance=None):
        super().__init__(jurisdiction_instance=jurisdiction_instance)  # Pass the required argument to BaseForm
        self.name = name
        self.abbreviation = abbreviation
        self.signature_type_allowed = signature_type_allowed
        self.hard_copy_required = hard_copy_required
        self.poa_allowed = poa_allowed
        self.tax_clearance_req = tax_clearance_req
        self.annual_reports_must_be_current = annual_reports_must_be_current
        self.signer_must_be_on_record = signer_must_be_on_record
        self.signer_titles_restricted = signer_titles_restricted
        #self.form_utility = FormUtility() # DALIA HELP # - is this necessary, or can we just use the instance from BaseForm or FormWizard class?

    # ... (Methods specific to jurisdiction)

# Subclass example
class Delaware(Jurisdiction):
    def __init__(self, *args, **kwargs):
        super().__init__('Delaware', 'DE', *args, **kwargs)
        # Texas-specific initialization

# ... (Other subclasses)
# Ensure each subclass for the states has meaningful differentiation; 
# otherwise, consider if the subclasses are necessary at all.
#  If they're only placeholders for now, it's okay to keep them as they are.