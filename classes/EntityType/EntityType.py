# entitytype.py

# EntityType: Subclasses for each entity type (e.g., LLC, Corporation, LP).
	#- Attributes: Fields specific to the entity type.
	#- Methods: Logic specific to the entity type.

# Inherits from BaseForm.
from ..BaseForm import BaseForm

class BaseEntityType(BaseForm):
    pass

class LLC(BaseEntityType):
    pass

class Corporation(BaseEntityType):
    pass

class LP(BaseEntityType):
    pass
