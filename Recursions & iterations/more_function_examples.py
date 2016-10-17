def foo(x, y = 5):
    def bar(x):
        return x + 1
    return bar(y * 2)
foo(3)

def goo(x, y = 5):
    def bar(x):
        return x + 1
    return bar(y * 2)
foo(3, 0)

def hoo(x):
    def bar (z, x = 0):
        return z + x
    return bar(3, x)

foo(2)

def foo (x):
    def bar (z, x = 0):
        return z + x
    return bar(3)

foo(5)

# recursive function scope example

def fact(n):
    '''

    :param n: if number is 1 then return 1 or else return number * fact(n-1)
    :return:
    '''
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(1))


'''
Iteration vs Recursion below... Factiorial_iter is an example of iteration and factorial is an example or recursion


'''

# Iteration
def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
