"CLASSES WITH MOSH"


class Point:
    "Point class"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        "compare two instance and check if values are greater than"
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        """Returns point Class instance"""
        return cls(0, 0)

    # def __str__(self):
    #     return f"({self.x}, {self.y})"

    def draw(self):
        """returns a string"""
        print(f"point({self.x}, {self.y})")


point = Point(20, 10)
other = Point(1, 2)

com = point + other
print(com.x)
