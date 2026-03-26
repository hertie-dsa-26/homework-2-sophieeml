import math
import unittest
from circle import Circle


class TestCirclePerimeter(unittest.TestCase):

    def test_perimeter_positive_radius(self):
        c = Circle(5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 5)

    def test_perimeter_radius_one(self):
        c = Circle(1)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi)

    def test_perimeter_radius_zero(self):
        c = Circle(0)
        self.assertAlmostEqual(c.perimeter(), 0)

    def test_perimeter_decimal_radius(self):
        c = Circle(2.5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 2.5)


class TestCircleArea(unittest.TestCase):

    def test_area_positive_radius(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), math.pi * 25)

    def test_area_radius_one(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), math.pi)

    def test_area_radius_zero(self):
        c = Circle(0)
        self.assertAlmostEqual(c.area(), 0)

    def test_area_decimal_radius(self):
        c = Circle(2.5)
        self.assertAlmostEqual(c.area(), math.pi * 2.5 ** 2)


if __name__ == "__main__":
    unittest.main()
