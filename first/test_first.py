import unittest
from first.first import *


class TestFindFactors(unittest.TestCase):

    def test_find_factors_of_1(self):
        self.assertEquals(find_factors(1), [1, 1])

    def test_find_factors_of_10(self):
        self.assertEquals(find_factors(10), [1, 2, 5, 10])

    def test_find_factors_of_prime_7(self):
        self.assertEquals(find_factors(7), [1, 7])

    # 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200.
    def test_find_factors_of_200(self):
        self.assertEquals(find_factors(200),
                          [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200])


class TestSliceCheck(unittest.TestCase):

    def test_single_letter(self):
        self.assertEquals(slice_check(['a'], 1), True)

    def test_no_repeats_fail(self):
        x = list('abc')
        self.assertEquals(slice_check(x, 1), False)
        self.assertEquals(slice_check(x, 2), False)
        self.assertEquals(slice_check(x, 3), True)

    def test_one_repeat_pass(self):
        x = list('abcabc')
        self.assertEquals(slice_check(x, 3), True)
        self.assertEquals(slice_check(x, 2), False)
        self.assertEquals(slice_check(x, 4), False)

    def test_repeats_with_extra_letters_fail(self):
        x = list('abcvvvabc')
        self.assertEquals(slice_check(x, 3), False)


class TestSolution(unittest.TestCase):

    def test_example_case_1(self):
        s = 'abcabcabcabc'
        self.assertEquals(solution(s), 4)

    def test_example_case_2(self):
        s = 'abccbaabccba'
        self.assertEquals(solution(s), 2)

    def test_all_same_letter(self):
        s = 'aaaaa'
        self.assertEquals(solution(s), 5)

    # the challenge specifies the max length for a string is 200
    def test_200_letters_all_same(self):
        s = 'a'*200
        self.assertEquals(solution(s), 200)

    def test_200_letters_repeating_sequence(self):
        s = 'abcd'*50
        self.assertEquals(solution(s), 50)


if __name__ == '__main__':
    unittest.main()
