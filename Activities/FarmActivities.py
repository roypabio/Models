from Fertilizing import Fertilizing

class FarmActivities:
    def __init__(self):
        self._fertilizing = None
    
    def addFertilizer(self, fertilizer):
        if self._fertilizing is None:
            self._fertilizing = Fertilizing()

        self._fertilizing.addFertilizer(fertilizer)
    
    def addIrrigation(self, irrigation):
        self._irrigation = irrigation
    