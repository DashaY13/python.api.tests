from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than or equal to 0")
        super().__init__(side_a, side_a)