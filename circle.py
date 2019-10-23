from shape import Shape


class Circle(Shape):

    r = None


    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        import math
        return (math.pi * self.r * self.r)

    def perimeter(self):
        import math
        return (self.r * 2 * math.pi)