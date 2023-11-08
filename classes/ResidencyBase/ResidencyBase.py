# residencybase.py

#3. Residency: Subclasses for each jurisdiction (Domestic, Foreign) under each EntityType.
	#- Attributes: Fields specific to the jurisdiction.
	#- Methods: Logic specific to the jurisdiction.

#Inherits from EntityType.

from ..EntityType import EntityType
from enums.residency import Residency as ResidencyStatus  # Renamed import to prevent naming conflicts

# Define 'determine_residency' as a top-level function - because it drives the logic of other class-based functions
def determine_residency(domestic_state):
    # Example logic, this will depend on your specific business rules
    if domestic_state == 'DE':  # Assuming 'DE' for Delaware, as an example
        return ResidencyStatus.DOMESTIC
    else:
        return ResidencyStatus.FOREIGN

# It's advisable to name the class something other than Residency to avoid conflicts
class ResidencyBase(EntityType):
    def __init__(self, domestic_state=None):
        self.domestic_state = domestic_state

class Domestic(ResidencyBase):
    # Additional domestic-specific attributes and methods
    pass

class Foreign(ResidencyBase):
    # Additional foreign-specific attributes and methods
    pass
