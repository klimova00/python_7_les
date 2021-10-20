from abc import ABC, abstractmethod


class Clothers(ABC):
    tissue_consumption = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothers):
    def __init__(self, height):
        self.height = height
        Coat.tissue_consumption += self.consumption

    def __str__(self):
        return f'Coat: Height: {self.height}, tissue_consumption: {self.consumption}, all_consumption_coat: {self.tissue_consumption}'

    @property
    def consumption(self):
        cons = self.height / 6.5 + 0.5
        return float(f'{cons:02f}')


class Costume(Clothers):
    def __init__(self, weight):
        self.weight = weight
        Costume.tissue_consumption += self.consumption

    def __str__(self):
        return f'Costume: Weight: {self.weight}, tissue_consumption: {self.consumption}, all_consumption_costume: {self.tissue_consumption}'

    @property
    def consumption(self):
        cons = (2 * self.weight + 0.3)
        return float(f'{cons:02f}')


my_clother_1 = Coat(54)
print(my_clother_1)
my_clother_2 = Costume(180)
print(my_clother_2)
my_clother_3 = Coat(40)
print(my_clother_3)
