class Road:

    _length = 0
    _width = 0

    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width
        self.weight = weight
        self.thickness = thickness

    def asphalt(self):
        result = (self._length * self._width * self.weight * self.thickness) / 1000
        print(f"{self._length} м * {self._width} м * {self.weight} кг * {self.thickness} см = {int(result)} т")


weight_asphalt = Road(20, 5000, 25, 5)
weight_asphalt.asphalt()
