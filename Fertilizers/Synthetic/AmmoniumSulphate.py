from Fertilizers.Synthetic.SyntheticFertilizer import SyntheticFertilizer

class AmmoniumSulphate(SyntheticFertilizer):

    def __init__(self, amount):
        self._amount = amount
        self._name = "Ammonium Sulphate"