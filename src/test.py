import unittest

from growth_Trend import trend

class TestCases(unittest.TestCase):
    def test(self):
        self.assertEqual(trend([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def test2(self):
        self.assertEqual(trend([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

if __name__ == '__main__':
    unittest.main()