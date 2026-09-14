from abc import abstractmethod

import figure


class Rectangle(figure.Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides can't be less than or equal to 0")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self) -> float:
        return self.side_a * self.side_b

    @abstractmethod
    def get_perimeter(self) -> float:
        return 2 * (self.side_a + self.side_b)