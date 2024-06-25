"CLASSES WITH MOSH"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        """Returns point Class instance"""
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        """returns a string"""
        print(f"point({self.x}, {self.y})")


point = Point.zero()
# point.draw()
print(point)


