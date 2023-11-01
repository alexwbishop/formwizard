# jurisdiction.py
#- Jurisdiction: Subclasses for each jurisdiction (e.g., US states, DC, Local jurisdictions)
	#- Attributes: Fields specific to the jurisdiction.
	#- Methods: Logic specific to the jurisdiction.

#Inherits from FilingType - need to import/define FilingType
from ..Utilities.FormUtility import FormUtility
from ..FilingType.filingtype import FilingType

class Jurisdiction(FilingType):
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
        self.form_utility = FormUtility()  # Now this should work

    @classmethod
    def create_jurisdiction(cls, name, abbreviation):
        # Here you can add default values for the other attributes if needed
        return cls(name, abbreviation, None, None, None, None, None, None, None, None)

    def some_method(self):
        self.form_utility.method_requiring_jurisdiction(self)


def some_method(self):
        self.form_utility.method_requiring_jurisdiction(self)

# ... (rest of your code for subclasses)


# Subclasses for each state and district
class Alabama(Jurisdiction):
    pass

class Alaska(Jurisdiction):
    pass

class Arizona(Jurisdiction):
    pass

class Arkansas(Jurisdiction):
    pass

class California(Jurisdiction):
    pass

class Colorado(Jurisdiction):
    pass

class Connecticut(Jurisdiction):
    pass

class Delaware(Jurisdiction):
    pass

class DistrictOfColumbia(Jurisdiction):
    pass

class Florida(Jurisdiction):
    pass

class Georgia(Jurisdiction):
    pass

class Hawaii(Jurisdiction):
    pass

class Idaho(Jurisdiction):
    pass

class Illinois(Jurisdiction):
    pass

class Indiana(Jurisdiction):
    pass

class Iowa(Jurisdiction):
    pass

class Kansas(Jurisdiction):
    pass

class Kentucky(Jurisdiction):
    pass

class Louisiana(Jurisdiction):
    pass

class Maine(Jurisdiction):
    pass

class Maryland(Jurisdiction):
    pass

class Massachusetts(Jurisdiction):
    pass

class Michigan(Jurisdiction):
    pass

class Minnesota(Jurisdiction):
    pass

class Mississippi(Jurisdiction):
    pass

class Missouri(Jurisdiction):
    pass

class Montana(Jurisdiction):
    pass

class Nebraska(Jurisdiction):
    pass

class Nevada(Jurisdiction):
    pass

class NewHampshire(Jurisdiction):
    pass

class NewJersey(Jurisdiction):
    pass

class NewMexico(Jurisdiction):
    pass

class NewYork(Jurisdiction):
    pass

class NorthCarolina(Jurisdiction):
    pass

class NorthDakota(Jurisdiction):
    pass

class Ohio(Jurisdiction):
    pass

class Oklahoma(Jurisdiction):
    pass

class Oregon(Jurisdiction):
    pass

class Pennsylvania(Jurisdiction):
    pass

class RhodeIsland(Jurisdiction):
    pass

class SouthCarolina(Jurisdiction):
    pass

class SouthDakota(Jurisdiction):
    pass

class Tennessee(Jurisdiction):
    pass

class Texas(Jurisdiction):
    pass

class Utah(Jurisdiction):
    pass

class Vermont(Jurisdiction):
    pass

class Virginia(Jurisdiction):
    pass

class Washington(Jurisdiction):
    pass

class WestVirginia(Jurisdiction):
    pass

class Wisconsin(Jurisdiction):
    pass

class Wyoming(Jurisdiction):
    pass


