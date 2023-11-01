# residency.py

#3. Residency: Subclasses for each jurisdiction (Domestic, Foreign) under each EntityType.
	#- Attributes: Fields specific to the jurisdiction.
	#- Methods: Logic specific to the jurisdiction.

#Inherits from EntityType.
from ..EntityType.entitytype import EntityType


class Residency(EntityType):
    pass

class Domestic(Residency):
    pass

class Foreign(Residency):
    pass
