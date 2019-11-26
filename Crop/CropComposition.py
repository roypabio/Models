class CropComposition:

    def  __init__(self, gross_energy, nitrogen_amount, dm_at_harvest, dm_marketable):
        self.gross_energy = gross_energy
        self.nitrogen_amount = nitrogen_amount
        self._dm_at_harvest = dm_at_harvest
        self._dm_marketable = dm_marketable

    def dry_matter_at_harvest(self):
        return self._dm_at_harvest.value

    def dry_matter_marketable(self):
        return self._dm_marketable.valueS
