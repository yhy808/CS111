#
# ps3pr4.py (Problem Set 3, Problem 4)        
#
# More algorithm design!
#

# function 1
def first_occur(seq, elem) :
    """ return the index of the first occurrence of elem in seq """
    if seq == '' or seq == []:
        return -1
    elif sum([1 for x in seq if x == elem]) == 0:
        return -1
    else:
        first_occur_rest = first_occur(seq[1:], elem)
        if seq[0] == elem:
            return 0
        else:
            return 1 + first_occur_rest
 
# function 2
def last_occur(seq, elem):
    """ return the index of the last occurrence of elem in seq """
    if seq == '' or seq == []:
        return -1
    elif sum([1 for x in seq if x == elem]) == 0:
        return -1
    else:
        last_occur_rest = last_occur(seq[:-1:-1], elem)
        if seq[-1] == elem:
            return len(seq) - 1
        else:
            return len(seq) - 1 + last_occur_rest

# function 3
def jscore(s1, s2):
    """ returns the Jotto score of s1 compared with s2 """
    if len(s1) == 1 and s1 in s2:
        return 1
    elif len(s1) == 1 and s1 not in s2:
        return 0
    elif s1 == [] or s2 == []:
        return 0
    else:
        jscore_rest = jscore(s1[1:], s2)
        def rem_first(elem, values):
            """ remove te first occurrence of elem from values """
            if values == []:
                return []
            elif values[0] == elem:
                return values[1:]
            else:
                rem_rest = rem_first(elem, values[1:])
                return [values[0]] + rem_rest
        if s1[0] in s2:
            return 1 + jscore(s1, rem_first(s1[0], s2))
        else:
            return jscore_rest











