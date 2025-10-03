class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0   


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

s = Shape()
print("Shape area:", s.area())         # 0

r = Rectangle(5, 3)
print("Rectangle area:", r.area())     # 15