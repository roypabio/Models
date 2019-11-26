class Crop:

    def __init__(self, characteristics, composition, productivity):
        self._characteristics = characteristics
        self._composition = composition
        self._productivity = productivity
    
    def crop_name(self):
        return self._characteristics.crop_name

    def crop_root_depth(self):
        return self._characteristics.crop_root_depth

    def crop_type(self):
        return self._characteristics.crop_name
