class Energy:

    def __init__ (self, amount, energy_type):
        self._amount = amount
        self._energy_type = energy_type

    def energy_type(self):
        return self._energy_type

    def amount(self):
        return self._amount
        
class Disel(Energy):

    def __init__(self, amount):
        self._amount = amount
        self._energy_type = "Disel"

class Electricity(Energy):

    def __init__(self, amount):
        self._amount = amount
        self._energy_type = "Electricity"