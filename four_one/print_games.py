#!/usr/bin/python2
from math import log
from sys import argv
from collections import deque

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
    return [[None]*len(guards)]*len(guards)


def fill_game_matrix(*guards):
    """Takes a list of guards and the corresponsing square
    matrix. Finds the result of each possible game and then
    records the number of spare guards resulting from that
    game in the matrix."""
    # In short, I like the stock


def parse_args(*guards):
    """Accepts multiple types of items and returns a single list
    containing all inputs.""" 
    # solution(1,1), you all are some cheeky monkeys
    output = list()
    for element in guards:
        if type(element) == list or type(element) == tuple:
            for item in element:
                output.append(item)
        else:
            output.append(int(element))
    return output


def make_pairs(guards):
    """Makes a 2d matrix representing pairs of players. Hopefully now 
    has 100 percent less alias driven bugs."""
    matrix = list()
    for i in range(len(guards)):
        matrix.append([0 for bunny in guards])
    return matrix


def set_game_results(m,guards):
    """Iterates over the pairs matrix and sets the individual cells to the
    result of each game's outcome. ***Causes side effects.***"""
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                m[i][j] = const_time_game(guards[i],guards[j])*2
            else:
                m[i][j] = None

def compare_to_all_others(bunny,guards):
    """Takes an integer representing the index of a bunny and returns a list
    holding the results of the banana_games between said bunny and all other 
    bunnies in the guards lists. Returns the indexes of all guards which
    create infinite loops with the specified bunny."""
    # bunny: int
    # guard: list<int>
    return [x for x in guards[:bunny]+guards[bunny+1:] if not const_time_game(x,guards[bunny])]



# def make_adjacency_lists:
#     """Makes an adjacency-lists representation of a graph for the given
#     list of guards. Returns a dictionary with the node as the key and its
#     adjacency-list as the value."""
#     # Shoutouts to Sedgewick
#     for i in range(len(guards)):



def solution(*guards):
    guards = parse_args(guards)
    
if __name__ == '__main__':
    x = [1, 7, 3, 21, 13, 19]
    y = compare_to_all_others(5,x)
    print y
    # x = parse_args(x)
    # m = make_pairs(x)
    # for row in m:
    #     print(row)
    # set_game_results(m,x)
    # print('\n')
    # for row in m:
    #     print(row)
    # fill_game_matrix(1,1,1)
    # for row in m:
    #     print(row)

