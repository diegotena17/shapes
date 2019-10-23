from shape import Shape


class RightTriangle(Shape):

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return ((self.a * self.b)/2)

    def perimeter(self):
        return (self.a + self.b + (self.a**2 + self.b**2)**0.5)

