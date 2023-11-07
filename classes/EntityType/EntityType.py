# entitytype.py

# EntityType: Subclasses for each entity type (e.g., LLC, Corporation, LP).
	#- Attributes: Fields specific to the entity type.
	#- Methods: Logic specific to the entity type.

# Inherits from BaseForm.
from ..BaseForm.BaseForm import BaseForm


class EntityType(BaseForm):
    pass

class LLC(EntityType):
    pass

class Corporation(EntityType):
    pass

class LP(EntityType):
    pass
