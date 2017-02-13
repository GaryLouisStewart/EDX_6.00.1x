def gen_powers(n):
    power = n 
    square_list = []
    for i in range(0,n+1):
        square_list.append(2 * i)
    return square_list

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exponential = 0
    temp_list = []
    final_list = []
    a = min(gen_powers(base))
    b = num(gen_powers(num))
    
    if a < 1:
        raise ValueError("Number must be a positive integer greater than 1")
    if b < 0:
        raise ValueError("Number must be a positive integer greater than 0")
        gen_powers(12)
Out[133]: 
[1,
 12,
 144,
 1728,
 20736,
 248832,
 2985984,
 35831808,
 429981696,
 5159780352,
 61917364224,
 743008370688,
 8916100448256]

def gen_powers(n):
    power = n 
    square_list = []
    for i in range(0,n+1):
        exponential = 0
        square_list.append(n ** exponential)
        exponential + 1
    return square_list


gen_powers(0)
Out[135]: [1]

def gen_powers(n):
    power = n 
    square_list = []
    for i in range(0,n):
        exponential = 0
        square_list.append(n ** exponential)
        exponential + 1
    return square_list


gen_powers(0)
Out[137]: []

gen_powers(1)
Out[138]: [1]
gen_powers(2)
Out[139]: [1, 1]
def gen_powers(n):
    power = n 
    square_list = []
    for i in range(0,n+1):
        exponential = 0
        square_list.append(n ** exponential)
        exponential + 1
    return square_list
    
    
    
    
    
