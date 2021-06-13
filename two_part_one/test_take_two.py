import unittest
from take_two import *


class MyTestCase(unittest.TestCase):

    def test_example_1(self):
        x = [2, 0, 2, 2, 0]
        self.assertEquals(solution(x), '8')

    def test_example_2(self):
        x = [-2, -3, 4, -5]
        self.assertEquals(solution(x), '60')

    def test_all_negative_odd_amount(self):
        x = [-2, -2, -2, -2, -2, -2, -2]
        self.assertEquals(solution(x), '64')

    def test_one_negative(self):
        x = [-2, 2, 2, 2]
        self.assertEquals(solution(x), '8')

    def test_all_zeros(self):
        x = [0, 0, 0]
        self.assertEquals(solution(x), '0')

    def test_single_negative_and_zeros(self):
        x = [-2, 0, 0, 0]
        self.assertEquals(solution(x), '0')


if __name__ == '__main__':
    unittest.main()
