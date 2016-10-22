'''

functions are first class objects and are often referred to as first class objects in programming
- they have types
- they can be elements of data structures like lists
- they  can appear in expressions
    - as part of an assignment statement
    - as an argument to a function.
- useful to use functions as arguments when coupled with lists (higher order programming)

'''


'''
* some helper functions below for factorial and fibonacci *
'''

def fib(x):
    '''
    :param x:
    :return:
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def fact(n):
    '''

    :param n: if number is 1 then return 1 or else return number * fact(n-1)
    :return:
    '''
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

# example function here

def applyToEach(N, o):
    '''
     assume that N is our list, o is the function mutates N
     by replacing each element, e, of N by o(e)
    '''
    for x in range(len(N)):
        N[x] = o(N[x])


N = [1, -2, 3.4]

applyToEach(N, abs)
print(N)

applyToEach(N, int)
print(N)

applyToEach(N, fact)
print(N)

applyToEach(N, fib)
print(N)


'''
*Lists of Functions*
- lets do things the other way
'''

def applyFuns(N, x):
    for r in N:
        print(r(x))

applyFuns([abs, int, fact, fib], 4)

'''
*Generalisation of Hops*
- python provides for us a general purpouse HOP, map
- simple form a unary function and a collection of suitable arguments
'''

L1 = [1, 28, 36]
L2 = [2, 57, 9]
for elt in map(min, L1, L2):
   print(elt)

''' some questions & revision '''

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
# example question... should return 5, -20, 40 & 45

testList = [1, -4, 8, -9]

def timesFive(a):
    return a * 5
applyToEach(testList, timesFive)

print testList


#1

testList = [1, -4, 8, -9]
def Abs(a):
    return abs(a)
applyToEach(testList, Abs)

print(testList)

#2

testList = [1, -4, 8, -9]

def Add1(a):
    return a + 1
applyToEach(testList, Add1)

print(testList)

#3

testList = [1, -4, 8, -9]

def Apply3(a):
    return abs(a * a)
applyToEach(testList, Apply3)

print(testList)

# something new

def applyToAll(M, y):
    result = []
    for x in range(len(M)):
        result.append(L[x](y))
    return result

