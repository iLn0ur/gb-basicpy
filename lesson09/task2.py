class Road:
    def __init__(self, _length=5000, _width=20):
        self._length = _length
        self._width = _width

    def square(self):
        return self._width * self._length * 25 * 5 / 1000


r = Road(500, 20)
print(f'масса асфальта {r.square()} т')
