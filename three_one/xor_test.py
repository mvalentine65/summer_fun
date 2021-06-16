#x = 1
#for i in range(2,129):
    #x = x ^ i
    #print("i:{} x:{}".format(i,x))


def xor_sum(limit):
    x = 0
    for i in range(1,limit+1):
        x = x ^ i
    return x


def iterative_xor(start,end):
    x = 0
    for i in range(start, end+1):
        x = x ^ i
    return x


def const_sum(target):
    x = target % 4
    if x == 0:
        return target
    elif x == 1:
        return 1
    elif x == 2:
        return target + 1
    else:
        return 0


def range_sum(start,end):
    if start < 1:
        start = 1
    """start should be greater than 0, end should be greater than start"""
    return const_sum(end)^const_sum(start-1)


def solution(start,length):
    current = start
    xor_total = 0
    for i in range(1,length+1):
        limit = length-i
        xor_total = xor_total ^ range_sum(current,current + (length-i))
        current += length
    return xor_total

# x = solution(0,3)
# y = solution(17,4)
# print(x)
# print(y)