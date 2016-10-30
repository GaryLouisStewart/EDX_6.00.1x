'''
purpose of this is to show lambda functions in python.
i've always wondered what that meant, apparently it just means calling a function with another function
who knew?!
'''

def func_filter(x):
    return x % 3 == 0
num4 = filter(func_filter, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print('Example 1: ') + '' + str(num4)

'''
or we can use a lambada function to solve the same problem
'''

num3 = filter(lambda y: y % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print('Example 2: ') + '' + str(num3)


def transform(z):
    return lambda x: x + z
g = transform(3)

print('Example 3: ') + '' + str(g(3))
print('Example 4: ') + '' + str(g(4))
print('Example 5: ') + '' + str(g(5))
print('Example 6: ') + '' + str(g(6))
print('Example 7: ') + '' + str(g(7))
