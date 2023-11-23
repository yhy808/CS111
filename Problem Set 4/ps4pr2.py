# 
# ps4pr2.py - Problem Set 4, Problem 2
#
# Using your conversion functions
#

from ps4pr1 import *

# function 1
def mul_bin(b1, b2):
    """ multiply the numbers and return the result in the form of a string that represents a binary number """
    return dec_to_bin(bin_to_dec(b1) * bin_to_dec(b2))

# function 2
def add_bytes(b1, b2):
    """ compute the sum of the two bytes and return that sum in the form of a string that represents an 8-bit binary number """
    sum_bin = dec_to_bin(bin_to_dec(b1) + bin_to_dec(b2))
    l = len(sum_bin)
    if l > 8:
        return sum_bin[l - 8:]
    elif l < 8:
        return (8 - l) * '0' + sum_bin
    else:
        return sum_bin
    
