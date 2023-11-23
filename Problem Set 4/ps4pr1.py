# 
# ps4pr1.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
#

# function 1
def dec_to_bin(n):
    """ takes a non-negative integer n and  returning a string version of the binary representation of that number """
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        dec_rest = dec_to_bin(n // 2)
        if n % 2 == 0:
            return dec_rest + '0'
        else:
            return dec_rest + '1'
        
        
# function 2
def bin_to_dec(b):
    """ takes a string b that represents a binary number and returning the resulting integer """
    if b == '0':
        return 0
    elif b == '1':
        return 1
    else:
        bin_rest = bin_to_dec(b[:-1])
        if b[-1] == '0':
            return 2 * bin_rest 
        else:
            return 2 * bin_rest + 1
        
        
