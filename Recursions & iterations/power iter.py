def iterPower(base, exp):
    '''

    :param base:
    :param exp:
    :return:
    '''
    result = 1
    while exp > 0:
       result *=base
       exp -= 1
    return result

print iterPower(1.2, 2)