import unittest
import utils

class TestUtils(unittest.TestCase):
    gifts = utils.parse_gifts(num_gifts=2)

    def test_haversine(self):
        haversine = utils.haversine_distance(self.gifts[0].pt, self.gifts[1].pt)
        self.assertEqual(int(haversine), 2440)

    def test_haversine_zero(self):
        haversine = utils.haversine_distance(self.gifts[0].pt, self.gifts[0].pt)
        self.assertEqual(int(haversine), 0)

    def test_gifts(self):
        five = utils.parse_gifts(num_gifts=5)
        self.assertEqual(len(five), 5)

if __name__ == '__main__':
    unittest.main()
