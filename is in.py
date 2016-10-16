def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetised string
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    m = aStr[len(aStr) // 2]
    if char == m:
       return True
    elif len(aStr) == 1:
        return False
    else:
       if char < m:
           return isIn(char, aStr[:len(aStr) // 2])
       elif char > m:
           return isIn(char, aStr[len(aStr) // 2:])
    return isIn(char, aStr)
# should return true if the character is in the String we give as input otherwise False
print isIn('a', 'abc')