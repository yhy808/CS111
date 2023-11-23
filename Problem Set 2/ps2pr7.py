# 
# ps2pr7.py - Problem Set 2, Problem 7
#
# Fun with recursion, part II
#

# function 1
def letter_score(letter):
    """ returns the value of that letter as a scrabble tile """
    assert(len(letter) == 1)
    if letter in ['q', 'z']:
        return 10
    elif letter in ['j', 'x']:
        return 8
    elif letter in ['k']:
        return 5
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter in ['b', 'c', 'm', 'p']:
        return 3
    elif letter in ['d', 'g']:
        return 2
    elif letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    else:
        return 0

# function 2
def scrabble_score(word):
    """ return the scrabble score of that string """
    if len(word) == 1:
        return letter_score(word)
    else:
        scrabble_score_rest = scrabble_score(word[1:])
        return letter_score(word[0]) + scrabble_score_rest

# function 3
def smaller_of(vals1, vals2):
    """ return a new list in which each element is the the smaller of the corresponding elements from the original lists """
    if len(vals1) == len(vals2) == 1:
        if vals1 < vals2:
            return vals1
        else:
            return vals2
    elif vals1 == [] or vals2 == []:
        return []
    else:
        smaller_of_rest = smaller_of(vals1[1:], vals2[1:])
        if vals1[0] < vals2[0]:
            return [vals1[0]] + smaller_of_rest
        else:
            return [vals2[0]] + smaller_of_rest
        
# function 4
def  merge(s1, s2):
     """ return a new string that is formed by “merging” together the characters in the strings s1 and s2 to create a single string """
     if len(s1) == len(s2) == 1:
         if s1 == s2:
             return s1
         else:
             return s1 + s2
     elif s1 == "":
         return s2
     elif s2 == "":
         return s1
     else:
         merge_rest = merge(s1[1:], s2[1:])
         if s1[0] == s2[0]:
             return s1[0] + merge_rest
         else:
             return s1[0] + s2[0] + merge_rest
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        