from figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be positive")

        # Условие существования треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Impossible triangle sides")

        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self) -> float:
        return self.a + self.b + self.c

    def get_area(self) -> float:
        # Формула Герона
        p = self.get_perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5