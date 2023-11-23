# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# More practice writing non-recursive functions
#

# function 1
def move_to_end(s, n):
    """ return the a new string in which the first n characters of s have been moved to the end of the string """
    return s[n:] + s[:n]

# function 2
def reverse_last(vals, n):
    """ return a new list in which the last n values of vals are reversed and all other values from vals remain in their original positions """
    if n < len(vals):
        return vals[:len(vals)-n] + vals[:-n-1:-1]
    else:
        return vals[::-1]
    

