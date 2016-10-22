# convert lists to strings and back again

#string example..
S = "I <3 cs"
print list(S)
print S.split('<')

# list example
L = ['a', 'b', 'c']
print ''.join(L)
print '_'.join(L)

# sorted list example

M = [9,6,0,3]
print sorted(M)
M.sort()
print M
M.reverse()
print M

# functions, Loops, range and lists

''' range is a special procedure it returns something which behaves like a tuple'''

print range(5) # equivialnt to tuple [0,1,2,3,4,]
print range(2,6) # equivilant to tuple [2,3,4,5]
print range(5,2,-1) # equivilant to tuple [5,4,3]