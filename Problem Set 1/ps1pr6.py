#
# ps1pr6.py - Problem Set 1, Problem 6
#
# Functions on strings and lists, part II
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

def reverse(s):
    """ returns a string in which the characters of s have been reversed """
    return s[-1::-1]

def ends_match(s):
    """  returns True if the first character in s matches the last character in s, and False otherwise """
    if s[0] == s[-1]:
        return True
    else:
        return False
    
def replace_start(values, new_start_vals):
    """ returns a new list in which the elements in new_start_vals have replaced the first n elements of the list values, 
        where n is the length of new_start_vals """
    return new_start_vals + values[len(new_start_vals):]

def adjust(s, length):
    """ returns a string in which the value of s has been adjusted 
        as necessary to produce a string with the specified length """
    if length > len(s):
        return s + s[-1] * (length - len(s))
    else:
        return s[0:length]
    
