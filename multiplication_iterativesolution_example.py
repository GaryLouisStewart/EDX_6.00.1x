def multiply_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
print multiply_iter(3,5)

