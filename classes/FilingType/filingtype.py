# filingtype.py

# FilingType: Subclasses for each filing type (e.g., Change of Agent, Incorporation) under each Jurisdiction.
	#- Attributes: Fields specific to the filing type.
	#- Methods: Logic specific to the filing type.

#Inherits from Residency (i.e. Domestic or Foreign).
from ..Residency.residency import Residency

class FilingType(Residency):
    pass

class ChangeOfAgent(FilingType):
    pass

class Registration(FilingType):
    pass

class Formation(FilingType):
    pass

class Amendment(FilingType):
    pass

class AnnualReport(FilingType):
    pass

class Dissolution(FilingType):
    pass

class Merger(FilingType):
    pass

class Conversion(FilingType):
    pass

class MiscInfoUpdate(FilingType):
    pass

class Reinstatement(FilingType):
    pass

class AssumedName(FilingType):
    pass
