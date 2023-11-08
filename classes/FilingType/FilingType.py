# filingtype.py

# FilingType: Subclasses for each filing type (e.g., Change of Agent, Incorporation) under each Jurisdiction.
# - Attributes: Fields specific to the filing type.
# - Methods: Logic specific to the filing type.

# Inherits from Residency (i.e. Domestic or Foreign).
from ..BaseForm import BaseForm

# Base class for all filing types
class BaseFilingType(BaseForm):
    pass

# Subclasses for each specific filing type
class ChangeOfAgent(BaseFilingType):
    pass

class Registration(BaseFilingType):
    pass

class Formation(BaseFilingType):
    pass

class Amendment(BaseFilingType):
    pass

class AnnualReport(BaseFilingType):
    pass

class Dissolution(BaseFilingType):
    pass

class Merger(BaseFilingType):
    pass

class Conversion(BaseFilingType):
    pass

class MiscInfoUpdate(BaseFilingType):
    pass

class Reinstatement(BaseFilingType):
    pass

class AssumedName(BaseFilingType):
    pass
