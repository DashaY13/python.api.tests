from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    @property
    def area(self) -> float:
        return self.get_area()

    @property
    def perimeter(self) -> float:
        return self.get_perimeter()

    def add_area(self, figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area() + figure.get_area()
