# convert lists to strings and back again, some tuples & other examples are included in this file.

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
print M.insert(0, 100)
print sorted(M)
M.sort()
print M
M.reverse()
print M

# functions, Loops, range and lists

''' range is a special procedure it returns something which behaves like a tuple '''

print range(5) # equivalent to tuple [0,1,2,3,4,]
print range(2,6) # equivalent to tuple [2,3,4,5]
print range(5,2,-1) # equivalent to tuple [5,4,3]

ListA = [1,4,3,0]
listB = ['x', 'z', 't', 'q']
print ListA.insert(0, 100)
print ListA.remove(3)
print ListA.append(7)
print ListA
print ListA + listB
print listB.sort()
print listB.pop()
print listB.count('a')
#print listB.remove('a')
print ListA.extend([4,1,6,3,4])
print ListA.count(4)
print ListA.index(1)
print ListA.pop(4)
ListA.reverse()
print ListA
print ListA is listB

# mutation, Aliasing, Cloning

'''

 *  Lists in memory *

 - lists are mutable, they behave differently than immutable types
 - is an object in memory
 - variable name points to object
 - any variable pointing to that object is affected
 - key phrase to keep in mind when working with lists is 'side effects'

'''

'''

*Aliases*

- hot is an alias for warm, this means that changing one will change the other
- append() has a side effect

'''

warm = ['red', 'yellow', 'orange']

print warm

hot = warm

print hot

hot.append('pink') # remember as stated in the comments above changing one will change the other

print hot
print warm

'''

*Print is not ==*
- if two lists print out the same thing, this does not necessarily
  mean that they are the same structure
- you can test if they are the same structure by mutating one and checking

'''

cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']
print(cool)
print(chill)

chill[2] = 'blue' # we now mutate to check if the structure is the same and you'll notice it isn't

print(cool)
print(chill)

# if the structure was the same then both lists would be modified however only the (chill) list has been modified


'''

*Cloning a List*
- create a new list and copy every element using chill = cool[:]
- useful when you want to change something in a list without modifying the original one

'''

cool = ['blue', 'green', 'grey']
chill = cool[:]


#mutate chill

chill.append('black')
print(chill)
print(cool)

'''
*sorting lists*
- calling sort() mutates the list for us but returns nothing
- calling sorted() does not mutate our list, and must assign result to a variable
'''

warm = ['red', 'yellow', 'orange']
sortedWarm = warm.sort()
print(warm)
print(sortedWarm)

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool)
print(cool)
print(sortedcool)

'''

*Lists of lists of lists*
lots of crazy stuff
;-)

- can have nested lists
- side effects are still possible after mutation

'''

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]

print(warm)
print(hot)
print(brightcolors)

brightcolors.append(hot)
print(brightcolors)

hot.append('pink')
print(hot)
print(brightcolors)

# or ;-)

print(hot+warm)

'''
*Mutation and Iteration*
- tip: avoid mutating a list if you are iterating over it

'''

def remove_dups(L1, L2):
    for x in L1:
        if x in L2:
            L1.remove(x)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)

print(L1)
print(L2)






