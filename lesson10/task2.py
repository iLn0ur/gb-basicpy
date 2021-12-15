from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, vh):
        self.vh = vh

    @abstractmethod
    def outlay(self):
        pass


class Coat(Clothes):
    def __init__(self, vh):
        self.vh = vh

    @property
    def outlay(self):
        return self.vh/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, vh):
        self.vh = vh

    def outlay(self):
        return 2 * self.vh + 0.3


coat = Coat(12)
print(coat.outlay)
suit = Suit(12)
print(suit.outlay())
