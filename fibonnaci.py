def fib(x):
    '''
    :param x:
    :return:
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
# should print out below 1, 2, 3, 5, 8, 13
print fib(1), fib(2), fib(3), fib(4), fib(5), fib(6)
