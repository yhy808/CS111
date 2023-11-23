# 
# ps4pr3.py - Problem Set 4, Problem 3
#
# Recursive operations on binary numbers
#

# function 1
def bitwise_and(b1, b2):
    """ compute the bitwise AND of the two numbers and return the result in the form of a string """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return len(b2) * '0'
    elif b2 == '':
        return len(b1) * '0'
    else:
        bitwise_and_rest = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return bitwise_and_rest + '1'
        else:
            return bitwise_and_rest + '0'
        
# function 2
def add_bitwise(b1, b2):
    """ adds two binary numbers """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        sum_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return sum_rest + '0'
        elif b1[-1] == '1' and b2[-1] == '0':
            return sum_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '1':
            return sum_rest + '1'
        else:
            return add_bitwise(sum_rest, '1') + '0'
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        