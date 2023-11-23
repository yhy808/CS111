# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def root(x):
    """ returns the square root of its input
        input x: any number (int or float)
    """
    return x ** 0.5

# function 2
def gap(num1, num2):
    """ returns the “gap” between two numeric inputs"""
    if num1 > num2:
        return num1 - num2
    if num1 < num2:
        return num2 - num1
    else:
        return 0

# function 3
def larger_gap(a1, a2, b1, b2):
    """ compute the gap between a1 and a2
        compute the gap between b1 and b2
        return the larger of the two gaps
    """
    def gap1(a1, a2):
        if a1 > a2:
            return a1 - a2
        if a1 < a2:
            return a2 - a1
        else:
            return 0
    def gap2(b1, b2):
        if b1 > b2:
            return b1 - b2
        if b1 < b2:
            return b2 - b1
        else:
            return 0
    if gap1(a1, a2) > gap2(b1, b2):
        return gap1(a1, a2)
    if gap1(a1, a2) <  gap2(b1, b2):
        return gap2(b1, b2)
    else:
        return gap1(a1, a2)

# function 4
def median(a, b, c):
    """ returns the median of the three inputs a, b, and c"""
    if a <= b <= c:
        return b
    if a <= c <= b:
        return c
    if b <= a <= c:
        return a
    if b <= c <= a:
        return c
    if c <= a <= b:
        return a
    if c <= b <= a:
        return b



# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
    
# test function with a sample test call for function 1
def test1():
     """ performs test calls on the functions above """
     print('root(25) returns', root(25))

# test function with a sample test call for function 2
def test2():
    """ performs test calls on the functions above """
    print ('gap(5, 2) returns', gap(5, 2))
    
# test function with a sample test call for function 3
def test3():
     """ performs test calls on the functions above """
     print('larger_gap(3, 2, 4, 7) returns', larger_gap(3, 2, 4, 7))

# test function with a sample test call for function 4
def test4():
    """ performs test calls on the functions above """
    print('median(10, 2, 7) returns', median(10, 2, 7))



