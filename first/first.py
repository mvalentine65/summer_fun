from math import sqrt


def find_factors(target):
    found = list()
    for i in range(1,int(sqrt(target))+1):
        if target % i == 0:
            found.append(i)
            found.append(target/i)
        found.sort()
    return found


def slice_check(array, size):
    if size > len(array)/2 and size != len(array):
        return False
    i = size
    limit = len(array)
    while i + size <= limit:
        if array[i:i+size] != array[0:size]:
            return False
        i += size
    return True


def solution(string):
    factors = find_factors(len(string))
    letters = list(string)
    for factor in factors:
        if slice_check(letters, factor):
            return len(string)/factor
