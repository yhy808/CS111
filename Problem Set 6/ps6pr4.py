# 
# ps6pr4.py - Problem Set 6, Problem 4
#
# Choosing the correct type of loop
#

# function 1
def log(b, n):
    """ return the logarithm to the base b of a number n """
    result = 0
    while n > 1:
        print('dividing', n, 'by', b, 'gives', n // b)
        n //= b
        result += 1
    return result
    
# function 2
def add_powers(m, n):
    """ add together the first m powers of n and that returns the resulting sum """
    result = 0
    for i in range(m):
        print(n, '**', i, '=', n ** i)
        x = n ** i
        result += x
    return result

# function 3
def negate_odds(values):
    """ all of its odd-valued elements are replaced with their negated values """
    for i in range(len(values)):
        if values[i] % 2 == 1:
            values[i] *= -1
