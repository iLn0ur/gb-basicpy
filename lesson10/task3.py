class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)
        else:
            return ValueError("разность не имеет значения")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __floordiv__(self, other):
        return Cell(self.count // other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, number):
        if self.count <= number:
            print('*' * self.count)
        else:
            i = self.count
            while i:
                if i <= number:
                    print("*" * i)
                    i = 0
                else:
                    print("*" * number)
                    i -= number
        print('\n')

    def __str__(self):
        return f"* {self.count}"


first = Cell(20)
second = Cell(10)
print(first - second)
print(first + second)
print(first * second)
print(first / second)
first.make_order(7)
second.make_order(4)
