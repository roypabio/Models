class Field:
    def __init__(self, land):
        self._machinery = list()
        self._infrastructure = list()
    
    def addLime(self, amount):
        self._lime  += amount
    
    def addDolomite(self, amount):
        self._dolomite += amount
    
    def addMachinery(self, machinery):
        self._machinery.append(machinery)
    
    def addInfrastructure(self, machinery):
        self._machinery.append(machinery)