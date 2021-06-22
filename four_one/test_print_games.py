import unittest
from print_games import banana_game
from print_games import find_gcd
from print_games import const_time_game


# I'm tired of writing this out by hand.
# Why did I ever do that?
# I am not a smart man.

class TestBananaGame(unittest.TestCase):
    
    def test_base_case_1_and_1(self):
        self.assertEquals(banana_game(1,1),True)
    
    def test_doubled_base_case_2and_2(self):
        self.assertEquals(banana_game(2,2),True)
    
    def test_shifted_case_1_and_3(self):
        self.assertEquals(banana_game(1,3),True)
    
    def test_looped_game_1_and_2(self):
        self.assertEquals(banana_game(1,2),False)
    
    def test_symmetry_1_and_3_mirrored(self):
        self.assertEquals(banana_game(1,3),banana_game(3,1))

    def test_symmetry_loop_1_and_2_mirrored(self):
        self.assertEquals(banana_game(1,2),banana_game(2,1))
    
    def test_multiple_of_1_and_3(self):
        self.assertEquals(banana_game(3,9),True)
    
    def test_two_rounds_out_1_and_7(self):
        self.assertEquals(banana_game(1,7),True)
    
    def test_two_rounds_out_shifted(self):
        self.assertEquals(banana_game(2,6),True)
        self.assertEquals(banana_game(3,5),True)
        self.assertEquals(banana_game(4,4),True)
    
    def test_multiple_of_two_rounds_12_and_84(self):
        self.assertEquals(banana_game(12,84),True)

    def test_three_rounds_out_1_and_15(self):
        self.assertEquals(banana_game(1,15),True)

class TestGCD(unittest.TestCase):
    
    def test_gcd_2_8(self):
        self.assertEquals(find_gcd(2,8),2)

    def test_gcd_88_77(self):
        self.assertEquals(find_gcd(88,77),11)

    def test_gcd_coprime_numbers(self):
        self.assertEquals(find_gcd(13,7),1)


class TestConstTimeGame(unittest.TestCase):

    def test_const_base_case(self):
        self.assertEquals(const_time_game(1,1),True)

    def test_const_base_case_double(self):
        self.assertEquals(const_time_game(2,2),True)
    
    def test_const_infinite_loop_1_and_2(self):
        self.assertEquals(const_time_game(1,2),False)
        self.assertEquals(const_time_game(2,1),False)

    def test_const_two_round(self):
        self.assertEquals(const_time_game(1,3),True)

    def test_multiple_of_two_round(self):
        self.assertEquals(const_time_game(3,9),True)
        self.assertEquals(const_time_game(50,150),True)

    def test_const_3_and_8_False(self):
        self.assertEquals(const_time_game(3,8),False)

    def test_const_two_round_mirrored(self):
        self.assertEquals(const_time_game(3,1),True)

    def test_const_three_round_with_shift(self):
        self.assertEquals(const_time_game(1,7),True)
        self.assertEquals(const_time_game(2,6),True)
        self.assertEquals(const_time_game(3,5),True)
        self.assertEquals(const_time_game(4,4),True)

if __name__ == '__main__':
    unittest.main()