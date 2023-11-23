# 
# ps6pr3.py - Problem Set 6, Problem 3
#
# Processing sequences with loops
#

# Function 1
def add_spaces(s):
    """ return the string formed by adding a space between each pair of adjacent characters in the string """
    result = ''
    for c in s:
        if c != s[-1]:
            result += c + ' '
    result += s[-1]
    return result

# Function 2
def merge(s1, s2):
    """ return a new string formed by “merging” together the characters in the strings s1 and s2 to create a single string """
    result = ''
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        if s1[i] != s2[i]:
            result += (s1[i] + s2[i])
        else:
            result += s1[i]
    if len(s1) < len(s2):
        result += s2[-(len(s2) - len(s1)):]
    if len(s1) > len(s2):
        result += s1[-(len(s1) - len(s2)):]
    return result

# Function 3
def contains(s, c):
    """ determine if s contains the character c, returning True if it does and False if it does not """
    for x in s:
        if x == c:
            return True
    return False

            
            
            
            
            
            
            
            
            
            
            