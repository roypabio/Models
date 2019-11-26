from Activities import FarmActivities

class FarmedCrop:

    def __init__(self, crop, field, farming_period, seed, crop_yield):
        self._crop = crop
        self._field = field
        self._farming_period = farming_period
        self._seed = seed
        self._crop_yield = crop_yield
        self._farm_activities = FarmActivities.FarmActivities()

    def addFertilizer(self, fertilizer):
        self._farm_activities.addFertilizer(fertilizer)

    def addIriigation(self, amount, irrig_type):
        self._farm_activities.addIrrigation(irrig_type, amount)

    def list_activities(self):
        return self._farm_activities.toList()
