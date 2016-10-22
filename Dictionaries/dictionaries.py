'''
example for dictionaries to help us store customer information
- so far we can store stuff using separate lists for all info in a database
- separate list for each item at the moment without a dictionary
- each list must have the same length
'''

''' * Without dictionaries *'''
names = ['Ana', 'John', 'Bob', 'James']
memebershipType = ['Bronze', 'Silver', 'Gold', 'Platinum']
membershipPoints = ['35', '55', '75', '95']


'''
- here is a messy function, too much info to keep track of, need many lists
- need to index always using integers
- must remember to change multiple lists
'''

def get_memberType(member, name_list, membertype_list, member_points):
    i = name_list.index(member)
    membershipType = membertype_list[i]
    membershipPoints = member_points[i]
    return (membershipType, membershipPoints)

''' * Dictionaries *
- stores pairs of data together (key + value)
- the 'key' will tell you the value to lookup

'''

# empty dictionary
mydict = {}
memberName = { '1': 'Ana', '2': 'John', '3': 'Bob', '4': 'James'}
memberType = { 'Ana': 'Bronze', 'John': 'Silver', 'Bob': 'Gold', 'James': 'Platinum'}
memberPoints = { 'Ana': '35', 'John': '55', 'Bob': '75', 'James': '95'}
'''
The memberType is our dictionary and the names = the keys where the Colours = the membership type
- now we can pull the values(Colours) back from the dictionary using the keys(names) of the people which
will return the customers name, membership type and their points
'''
print(memberName['1']) + ' ' + str(memberType['Ana']) + ' ' + str(memberPoints['Ana'])
print(memberName['2']) + ' ' + str(memberType['John']) + ' ' + str(memberPoints['John'])
print(memberName['3']) + ' ' + str(memberType['Bob']) + ' ' + str(memberPoints['Bob'])
print(memberName['4']) + ' ' + str(memberType['James']) + ' ' + str(memberPoints['James'])

# see how much easier that was ;-)

# now we can do some testing and modify our dictionaries

# test to see if a customer is in our dictionary (bool) will return True if yes and false if no
print('Ana' in memberName.values())
print('John' in memberName.values())
print('Gary' in memberName.values())

# memberName['Jerry'] = this will give a KeyError as Jerry is not in the dictionary but we can add him to it
memberName['5'] = 'Jerry'
print memberName['5']

''' * Dictionary Operations *
- get an iterable that acts like a tuple of all keys
- get an iterable that acts like a tuple of all values
'''

print(sorted(memberName.keys()))
print(sorted(memberType.keys()))
print(sorted(memberPoints.keys()))

print(sorted(memberName.values()))
print(sorted(memberType.values()))
print(sorted(memberPoints.values()))

'''
- values
    - mutable and immutable (any type)
    - can be duplicates
    - dictionary values could be lists and even other dictionaries
- keys
    - must be unique
    - immutable type (int, float, string, tuple, bool)
        - needs to be object that is hashable but immutable as immutable types are all hashable
    - BE CAREFUL with float type as a key
- NO Order to keys or values
'''

