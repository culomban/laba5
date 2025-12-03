import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_3(self):
        res = area(3)
        self.assertAlmostEqual(res, 9 * math.pi)

    def test_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_5(self):
        res = area(5)
        self.assertEqual(res, 25 * math.pi)

    def test_perimeter_1(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_5(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)

    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_3(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 6 * math.pi)

