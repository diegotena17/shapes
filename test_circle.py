import unittest

import circle
class TestCircle(unittest.TestCase):

    def setUp(self):
        print("SetUp")

    def test_Circl(self):
        circl = circle.Circle(2)
        data = circl.summary()
        self.assertEqual(12.566370614359172, data['area'])
        self.assertAlmostEqual(12.566370614359172, data['perimeter'])

