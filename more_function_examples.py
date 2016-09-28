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