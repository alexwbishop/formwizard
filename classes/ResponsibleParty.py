# responsibleparty.py
#
#
from address import Address

class ResponsibleParty:
    def __init__(self, first, mid, last, title, is_director, address: Address):
        self.first_name = first
        self.mid_name = mid
        self.last_name = last
        self.address = address
        self.title = title
        self.is_director = is_director
