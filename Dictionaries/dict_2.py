random_dict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f'}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for value in aDict.values():
        result += len(value)
    return result
print(how_many(random_dict))


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    v = list(aDict.values())
    k = list(aDict.keys())
    return k[v.index(max(v))]
print(biggest(animals))

'''
*Fibonacci and dictionaries*
- here below is an example of fibonacci with a dictionary

'''

def fib_dict(a, b):
    if a in b:
        return b[a]
    else:
        ans = fib_dict(a-1, b) + fib_dict(a-2, b)
        b[a] = ans
        return ans
b = {1:1, 2:2}
print(fib_dict(6, b))


'''
lets do some testing first of all.
'''

def fib(a):
    global numFibCalls
    numFibCalls += 1
    if a == 1:
        return 1
    elif a == 2:
        return 2
    else:
        return fib(a-1) + fib(a-2)

def fib_dictionary(a, b):
    global numFibCalls
    numFibCalls += 1
    if a in b:
        return b[a]
    else:
        ans = fib_dictionary(a-1, b) + fib_dictionary(a-2, b)
        b[a] = ans
        return ans
numFibCalls = 0
fibArg = 34

print(fib(fibArg))
print('function calls', numFibCalls)

# the method below is the most efficient in getting our results back have a look at the number of function calls that it makes
numFibCalls = 0
d = {1:1, 2:2}
print(fib_dictionary(fibArg, d))
print('function calls', numFibCalls)

