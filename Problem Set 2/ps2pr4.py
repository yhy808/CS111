# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# Fun with recursion, part I
#

# function 1
def repeat(s, n):
    """ return a string in which n copies of s have been concatenated together """
    if n == 0:
        return ""
    else:
        repeat_rest = repeat(s, n-1)
        return s + repeat_rest
    
# function 2
def contains(s, c):
    """ determine if s contains the character c, returning True if it does and False if it does not """
    if s == "":
        return False
    else:
        con_rest = contains(s[1:], c)
        if s[0] == c:
            return True
        else:
            return con_rest

# function 3
def add(vals1, vals2):
    """ return a new list in which each element is the sum of the elements at the corresponding positions in the original lists """
    if len(vals1) != len(vals2):
        return []
    else:
        if len(vals1) == 1:
            return [vals1[0] + vals2[0]]
        else:
            add_rest = add(vals1[1:],vals2[1:])
            return [vals1[0] + vals2[0]] + add_rest


