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


class TestMatrixFunctions(unittest.TestCase):
    case_1 = [  [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] ]
    
    info_1 = ([2,3,4,5],[0,1],{0:2,1:7})
    
    case_2 = [  [0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0] ]

    info_2 = ([2,3,4],[0,1],{0:3,1:7})

    def test_copy_matrix(self):
        x = list([[0],[1]])
        y = copy_matrix(x)
        self.assertEquals(y,x)
        x[0] = [5]
        self.assertNotEqual(y,x)

    def test_case_1(self):
        case_1 = [  [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] ]
    
        info_1 = ([2,3,4,5],[0,1],{0:2,1:9})
        R_1 = [[0,0,0,fractions.Fraction(1,2)],
                [0,fractions.Fraction(3,9),fractions.Fraction(2,9),0]]
        Q_1 = [[1,fractions.Fraction(-1,2)],
                [fractions.Fraction(-4,9),1]]

        self.assertEquals(parse_to_standardized_form(case_1),info_1)
        self.assertEquals(make_r_i_minus_q(info_1[0],info_1[1], case_1,info_1[2]),(R_1,Q_1))
    def test_case_2(self):
        case_2 = [  [0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0] ]

        info_2 = ([2,3,4],[0,1],{0:3,1:7})
        R_2 = [ [fractions.Fraction(1,3),0,0],
                [0,fractions.Fraction(3,7),fractions.Fraction(4,7)] ]
        Q_2 = [ [1,0-fractions.Fraction(2,3)],
                [0,1] ]
        self.assertEquals(parse_to_standardized_form(case_2),info_2)
        self.assertEquals(make_r_i_minus_q(info_2[0],info_2[1], case_2,info_2[2]),(R_2,Q_2))




if __name__ == '__main__':
    unittest.main()