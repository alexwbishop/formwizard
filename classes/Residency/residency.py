# residency.py

#3. Residency: Subclasses for each jurisdiction (Domestic, Foreign) under each EntityType.
	#- Attributes: Fields specific to the jurisdiction.
	#- Methods: Logic specific to the jurisdiction.

#Inherits from EntityType.
from ..EntityType.entitytype import EntityType


class Residency:
    def __init__(self, domestic_state=None):
        self.domestic_state = domestic_state

class Domestic(Residency):
    pass

class Foreign(Residency):
    pass

