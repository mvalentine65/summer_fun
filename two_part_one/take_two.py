from operator import mul
"""Unoptimized solution. Currently this more memory than it should.
Making seperate lists for the positive and the negative numbers 
uses n space and it could be done in constant space with a handful
of values and some more if statements. There's probably an 'elegant'
algorithm for this I just haven't found. It feels kinda like a twist
on the House Robber dynamic question, but the negatives really complicate
things."""

def check_negatives(array):
    if len(array) < 2:
        return 0
    product = reduce(mul, array, 1)
    if product < 0:
        arr = sorted(array,reverse=True)
        product /= arr[0]
    return product


def check_positives(array):
    if len(array) == 0:
        return 0
    return reduce(mul, array, 1)


def solution(xs):
    positives = list()
    negatives = list()
    for panel in xs:
        if panel > 0:
            positives.append(panel)
        elif panel < 0:
            negatives.append(panel)
    positive_product = check_positives(positives)
    negative_product = check_negatives(negatives)
    if not positive_product and not negative_product:
        return '0'
    elif positive_product and not negative_product:
        return str(positive_product)
    elif not positive_product and negative_product:
        return str(negative_product)
    else:
        return str(positive_product*negative_product)    
# More 'if's than need be
# My shame glows bright in the night
# If it works, it works

if __name__ == '__main__':
    x = [-2, -2, -2, -2, -2, -2, -2]
    print(solution(x))
