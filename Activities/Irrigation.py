from ValueObjects import Energy

class Irrigation:

    def __init__(self, irrigation_technique, water_applied):
        self._technique = irrigation_technique
        self._water_applied = water_applied
        self._energyUseList = list()
    
    def addEnergyUse(self, energy):
        self._energyUseList.append(energy)

    def getDiselEnergyAmount(self):
        if len(self._energyUseList) < 1 :
            return Energy.Disel(0) # calculate  actual by formula
        else :
           disel_energy =[ x.amount() for x in  x.self._energyUseList if x.energy_type() == "Disel"]
           return sum(disel_energy)

    def getElectricEnergyAmount(self):
        if self._energyUseList is None or len(self._energyUseList) < 1:
            return Energy.Disel(0) # calculate by formula
        else :
           disel_energy =[ x.amount() for x in  x.self._energyUseList if x.energy_type() == "Electricity"]
           return sum(disel_energy)
