from Fertilizers.Fertilizer import Fertilizer

class SyntheticFertilizer(Fertilizer):

    def __init__(self, name, amount):
        self._name = name
        self._amount = amount
        self._type = "Synthetic"