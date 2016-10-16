def fourthPower(x):
    '''
    :param x: multiples the number to the fourth power
    :return: returns the number to the power of 4 (4**4)
    '''
    def square(x):
        '''
        :param x:
        :return:
        '''
        return x * x
    y = square(x) * square(x)
    return y
num = 4
result = fourthPower(num)
print str(num) + " to the power of 4 is: ..." + str(result)
