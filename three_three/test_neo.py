import unittest
from neo import *

class TestGCD(unittest.TestCase):

    def test_gcd_2_8(self):
        self.assertEquals(gcd(2,8),2)

    def test_gcd_88_77(self):
        self.assertEquals(gcd(88,77),11)

    def test_gcd_coprime_numbers(self):
        self.assertEquals(gcd(13,7),1)


class TestLCM(unittest.TestCase):

    def test_lcm_same_number(self):
        self.assertEquals(lcm(8,8),8)

    def test_lcm_5_10(self):
        self.assertEquals(lcm(5,10),10)

    def test_lcm_300_1000(self):
        self.assertEquals(lcm(300,1000), 3000)

    def test_lcm_coprime_primes(self):
        self.assertEquals(lcm(23,11), 23*11)

    def test_lcm_coprime_numbers(self):
        self.assertEquals(lcm(10,21), 210)


if __name__ == '__main__':
    unittest.main()