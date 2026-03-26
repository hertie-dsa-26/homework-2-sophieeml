import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2