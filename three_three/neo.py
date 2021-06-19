 import fractions

# Whoa, I know linear algebra...
# Don't tell me, show me.

# TODO: finish function make_r_q
# TODO: implement matrix inversion function (gaussian vs cofactors)
# TODO: implement matrix  multiplication function
#       ---I only need to multiply s[0] to find the outcomes I need
# TODO: convert s[0] probabilities to outcome array
# TODO: make gains
# TODO: ???
# TODO: profit
def gcd(a,b):
    """Given two numbers, returns the greatest common denominator"""
    while a%b != 0:
        a,b = b, a%b
    return b


def lcm(a,b):
    """Given two numbers, returns the least common multiple"""
    return a*(b/gcd(a,b))


def find_array_denominator(array):
    """Takes the int array for each state and returns the total of
    all the ints. This can be used as the denominator in the fraction
    conversion. If the denominator is zero, Sky-Net has begun
    it's assualt, and this array is a terminator array."""
    return sum(array)


def convert_array_to_fractions(array, denom):
    """Convert the numbers in an array to fractions. Iterates
    over each value sets it to a fraction with the value 
    as the numerator."""
    size = len(array)
    output = [None]*size
    for i in range(size):
        output[i] = fractions.Fraction(array[i],denom)
    return output


def make_identity_matrix(size):
    """Make a 2d identity matrix with a length and height 
    equal to size. Takes integer argument and returns an
    Fraction[][] with 1/1 along the diagnol."""
    output = list()
    for i in range(size):
        next = list()
        for j in range(size):
            if i != j:
                next.append(fractions.Fraction(0,1))
            else:
                next.append(fractions.Fraction(1,1))
        output.append(next)
    return output


def copy_matrix(matrix):
    """Returns a value copy of the 2-d array passed to the function."""
    return [row[:] for row in matrix]


# def make_r_q(index_list, m, denoms):
#     output = list()
#     for i in index_list:
#         #denominator d
#         d = denoms[i]
#         row = list()
#         for t in  


def solution(m):
    if sum(m[0]) == m[0][0]:
        return [1,1]
    # lists of y-indexes in the matrix to sort absorbing vs transient
    terminators = list()
    transients = list()
    # index:denominator dictionary
    denoms = dict()
    # if sum(array) == 0, then the array is a terminators,
    # push to appropriate submatrix
    for i in range(len(m)):
        denom = find_array_denominator(m[i])
        if denom == 0:
            terminators.append(i)
        else:
            transients.append(i)
        denoms[i] = denom
    Q = make_Q_array(terminators,transients,m)
    