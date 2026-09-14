import math
from figure import Figure


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Circle radius can't be less than or equal to 0")
        self.r = r

    def get_area(self) -> float:
        return math.pi * (self.r ** 2)

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.r