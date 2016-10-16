def odd(x):
    '''

    :param x: if number divide by two has a remainder of 0 then it is odd otherwise even
    :return: return the number % 2 if the remainder is greater than 0 then the number is even
    '''
    while x % 2 == 0:
        return False
    else:
        return True

print odd(6)