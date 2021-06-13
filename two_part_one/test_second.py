import unittest
from two_part_one.second import solution
# this folder used to be named 'second'
# turns out this causes a name collision or something
# go figure


class TestSecond(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
