import unittest

import triangle
class TestTriangle(unittest.TestCase):

    def setUp(self):
        print("SetUp")

    def test_Tri(self):
        tri = triangle.Triangle(2, 4, 4)
        data = tri.summary()
        self.assertEqual(3.872983346207417, data['area'])
        self.assertAlmostEqual(10., data['perimeter'])
