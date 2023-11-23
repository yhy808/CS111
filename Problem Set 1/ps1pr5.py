#
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

def last_first(values):
    """ returns a new list containing the last value followed by the first value """
    last = values[-1]
    first = values[0]
    return [last, first]

def every_other(values):
    """ returns a list containing every other value from the original list """
    return values[0::2]

def begins_with(word, prefix):
    """ returns True if the string word begins with the string prefix, and False otherwise """
    if word[0:len(prefix)] == prefix:
        return True
    else:
        return False
    
    
    
    

