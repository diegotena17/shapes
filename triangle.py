# coding: utf8
from shape import Shape


class Triangle(Shape):
    """
    Triangle shape.
    """

    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c)/2;
        return (s * (s - self.a) * (s-self.b) * (s-self.c))**0.5

    def perimeter(self):
        return  (self.a + self.b + self.c)