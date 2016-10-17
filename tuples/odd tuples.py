def oddTuples(aTup,):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    rTup = ()
    index = 0

    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2
    return rTup
print oddTuples(('I', 'am', 'a', 'test', 'tuple'))


# simple way to solve the problem below using tuple slicing by 2 to achieve the same result as above
def oddTuples2(atup):
    return atup[::2]
print oddTuples2(('I', 'am', 'a', 'test', 'tuple'))