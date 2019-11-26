from datetime import timedelta

class CropProductivity:

    def __init__(self, nursery_duration, sapling_yield, cultiv_duration, orch_density, fallow_period, non_bear_duration):
        self._nursery_duration =  nursery_duration
        self._sapling_yield = sapling_yield
        self._cultiv_duration = cultiv_duration
        self._orch_density = orch_density
        self._fallow_period = fallow_period
        self._non_bear_duration = non_bear_duration