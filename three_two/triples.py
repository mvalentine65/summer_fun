def left_search(array, index):
    """Search array[0:i] for elements which are a factor
    of array[i]. Returns the number of factors found as an int."""
    factors = 0
    for num in array[0:index]:
        factors += (array[index] % num == 0)
    return factors


def right_search(array,index):
    """Search array[i+1:] for elements which are divisible by
    array[index]. Returns the number of factors found as an int."""
    products = 0
    for num in array[index+1:]:
        products += (num % array[index] == 0)
    return products

def solution(l):
    triplets = 0
    for i in range(1,len(l)):
        triplets += left_search(l,i) * right_search(l,i)
    return triplets

if __name__ == '__main__':
    x = solution([1,1,1])
    y = solution([1,2,3,4,5,6])
    print(x)
    print(y)