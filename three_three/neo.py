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


def  parse_to_standardized_form(m):
    """ Given a 2-d matrix in non-standard form, returns a tuple containing
    two lists and a dictionary. The tuple[0] is a list of the indexes of all
    absorbing states, and tuple[1] is a list of the transient states. Tuple[2]
    is a dictionary containing the transient indexes and the sum of their 
    elements.""" 
    denoms = dict()
    terminators = list()
    transients = list()    
    for i in range(len(m)):
        denom = find_array_denominator(m[i])
        if denom == 0:
            terminators.append(i)
        else:
            transients.append(i)
            denoms[i] = denom
    return (terminators,transients,denoms)

def make_r_i_minus_q(absorbing, limited, matrix, denoms):
    """ Takes a non-standard matrix and outputs the subarrays
    R and Q according to standard form. Absorbing and limited
    are lists holding the indexes of their respective states,
    matrix is the non-standard 2-d matrix, and denoms is a
    dictionary containing indexes as keys and the number of total
    possible outcomes as the value. Returns a tuple (R,I-Q).""" 
    R = list()
    Q = list()
    # make Q limited->limited array
    # why iterate over this twice when I can make I-Q here?
    for l in limited :
        #denominator d
        d = denoms[l]
        row = list()
        for ll in limited:
            if l == ll:
                row.append(1-fractions.Fraction(matrix[l][ll],d))
            else:
                row.append(0-fractions.Fraction(matrix[l][ll],d))
        Q.append(row)
    # make R limited->absorbing array
    for  l in limited:
        d = denoms[l]
        row = list()
        for a in absorbing:
            row.append(fractions.Fraction(matrix[l][a],d))
        R.append(row)
    return (R,Q)

def invert_matrix(Q):
    """ Given a 2-d matrix Q, uses gaussian elmination to find the
    algebraic inverse of Q. """
    size = len(Q)
    I = make_identity_matrix(size)
    for i in range(size):
        # if past the first row, check previous row and zero the
        # appropriate element
        if i > 0:
            multiplier = Q[i][i-1]
            if multiplier != 0:
                for j in range(size):
                    Q[i][j] = Q[i][j] - multiplier*Q[i-1][j]
                for j in range(size):
                    I[i][j] = I[i][j] - multiplier*I[i-1][j]
        # Find element on the diagnol...
        multiplier = 1/Q[i][i]
        # if element not equal to one, multiply row by 1/element
        if multiplier != 1:
            for j in range(size):
                Q[i][j] = Q[i][j] * multiplier
                # mirror the multiplication in the identity matrix
                I[i][j] = I[i][j] * multiplier
        # iterate over all previous rows and zero the element at Q[_][i]
        for row in range(i):
            multiplier = Q[row][i]
            # if Q[_][i] not 0, subtract for row to make it zero
            if multiplier != 0:
                for j in range(size):
                    Q[row][j] = Q[row][j] - multiplier*Q[i][j]
                # mirror subtraction in identity matrix
                    I[row][j] = I[row][j] - multiplier*I[i][j]

                # for element in I[row]:
                #     element = element - multiplier*I[i][i]
    return I


def multiply_matrix(Q, R):
    output = list()
    for i in range(len(R[0])):
        total = 0
        for j in range(len(R)):
            total += Q[0][j] * R[j][i]
        output.append(total)
    return output


def make_answer(output):
    """Finds the lcm of the denominators in output. Converts the fractions to whole numbers
    and appends the lcm to the end of output."""
    least = 1
    for num in output:
        least = lcm(least,num.denominator)
    for i in range(len(output)):
        output[i] = int(output[i]*least)
    output.append(least)
    return output


def solution(m):
    ########################### Housekeeping ############################
    # if initial state s[0] is absorbing state, return appropriate value 
    if sum(m[0]) == m[0][0]:
        return [1,1]
    terminators,transients,denoms = parse_to_standardized_form(m)
    #################### Math time ######################
    R,Q = make_Q_array(terminators,transients,m, denoms)
    Q = invert_matrix(Q)


if __name__== "__main__":
    case_1 = [  [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] ]
    a_1, t_1, denoms = parse_to_standardized_form(case_1)
    r_1, q_1 = make_r_i_minus_q(a_1,t_1,case_1,denoms)
    # for a in r_1:
    #     print(a)
    # for b in q_1:
    #     print(b)
    y = invert_matrix(q_1)
    x = multiply_matrix(y,r_1)
    print(x)
    answer = make_answer(x)
    print(answer)