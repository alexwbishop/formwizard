# responsibleparty.py
#
#
from address import Address

class ResponsibleParty:
    def __init__(self, first, mid, last, address: Address):
        self.first_name = first
        self.mid_name = mid
        self.last_name = last
        self.address = address
