#x = 1
#for i in range(2,129):
    #x = x ^ i
    #print("i:{} x:{}".format(i,x))


def xor_sum(limit):
    x = 0
    for i in range(1,limit+1):
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


def iterative_xor(start,end):
    x = 0
    for i in range(start, end+1):
        x = x ^ i
    return x


a = 5
b = 10
x = xor_sum(a)
y = xor_sum(b)
# print('start sum ' + str(x))
# print('end sum ' + str(y))
# print('test ' + str(xor_sum(b)^xor_sum(a-1)))
# print(5^6^7^8^9^10)
print(const_sum(4))
print(const_sum(10))
print(5^6^7^8^9^10)
print(const_sum(10)^const_sum(5-1))