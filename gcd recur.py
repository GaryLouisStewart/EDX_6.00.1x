def gcdRecur(a, b):
    '''
    a, b positive integers
    returns: positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
print gcdRecur(2, 12)

# example 2
def gcdRecur(a, b):
    '''
    :param a:
    :param b:
    :return:
    '''
    if b > a:
        return gcdRecur(b, a)
    r = a%b
    if r == 0:
        return b
    return gcdRecur(r, b)
print gcdRecur(17, 12)