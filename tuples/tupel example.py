# the following is an example of a tuple.

x = (1, 2, (3, 'John', 4), 'Hi')
print '1)', x[0]
print '2)', x[2]
print '3)', x[-1]
print '4)', x[2][2]
print '5)', x[2][-1]
print '6)', x[-1][-1]
# {this one will error out on purpose} print '7)', x[-1][2]
print '8)', x[0:1]
print '9)', x[0:-1]
print '10)', len(x)
print '11)', 2 in x
print '12)', 3 in x
# {this one errors out on purpose too} print '13)', x[0] = 8

