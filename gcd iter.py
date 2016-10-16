def gcdIter(a, b):
    '''

    :param a:
    :param b:
    :return:
    '''
    if (a>b):
        n=a
        a=b
        b=n
    while (b!=0):
        z=b
        b=a%z
        a=z
    return a
print gcdIter(2, 12)