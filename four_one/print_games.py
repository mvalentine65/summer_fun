#!/usr/bin/python2
from math import log
from sys import argv


def find_gcd(a,b):
    """This time it accepts arguments in either order."""
    big,small = max(a,b),min(a,b)
    while big%small != 0:
        big,small = small, big%small
    return small


def const_time_game(lesser,greater):
    """Experimental function which determines outcome
    in constant time instead of iterating over each game
    round until a winner is found. If the sum of the guards'
    bananas is multiple of a power of 2, then the game extends
    from the 1:1 base case for failure."""
    # factor the total to account for the 3:9 game
    total = (lesser + greater)/find_gcd(lesser,greater)
    return log(total,2) % 1 == 0



def banana_game(i, j):
    """Simulates the game as defined in the question.txt file.
    Arguments i and j are the starting values of the guards. Returns
    True if the game termintates, and returns False if the game is 
    an infinite loop."""
    # past_rounds holds banana numbers for old rounds
    # if a result exists in the dictionary, this round has been played before
    # this means a loop has occured, so return false
    past_rounds = dict()
    while not past_rounds.get(i) and not past_rounds.get(j):
        if i == j:
            return True
        past_rounds[i] = j
        past_rounds[j] = i
        if i > j:
            i = i - j
            j = 2*j
        else:
            j = j - i
            i = 2*i
    return False

def make_game_matrix(guards):
    """This function accepts a list of integers and returns a 
    square 2d matrix based on the size of the list."""
    # size = len(guards)
    return [[0]*len(guards)]*len(guards)


# if __name__ == '__main__':
#     if len(argv) == 3:
#         lower, upper = 1, int(argv[2])
#     elif len(argv) == 4:
#         lower, upper = int(argv[2]), int(argv[3])
#     else:
#         lower, upper = 1, 32
#     #
#     #for i in range(lower, upper+1):
        #iterate_tests(i)



