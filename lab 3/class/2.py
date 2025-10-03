class Shape:
    def __init__(self):
        pass  

    def area(self):
        return 0   


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

s = Shape()
print("Shape area:", s.area())   # 0

sq = Square(5)
print("Square area:", sq.area())  # 25