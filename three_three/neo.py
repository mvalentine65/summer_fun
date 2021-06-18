import fractions

# Whoa, I know linear algebra...
# Don't tell me, show me.


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
    return [row[:] for row in x]
