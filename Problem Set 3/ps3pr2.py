# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design
#

# function 1
def cube_evens_lc(values):
    """ return a list containing the cubes of the even numbers in values """
    lc = [x ** 3 for x in values if x % 2 == 0]
    return lc

# function 2
def cube_evens_rec(values):
    """ return a list containing the cubes of the even numbers in values """
    if values == []:
        return []
    else:
        cube_evens_rest = cube_evens_rec(values[1:])
        if values[0] % 2 == 0:
            return [values[0] ** 3] + cube_evens_rest
        else:
            return cube_evens_rest

# function 3
def num_occur(c, s):
    """ returns the number of times that c occurs in s """
    if s == "":
        return 0
    else:
        num_occur_rest = num_occur(c, s[1:])
        if c == s[0]:
            return 1 + num_occur_rest
        else:
            return num_occur_rest
        
# function 4
def most_occur(c, words):
    """ returns the string in the list with the most occurrences of c """
    scored_num = [[num_occur(c,s), s] for s in words]   
    bestpair = max(scored_num)
    return bestpair[1]

# function 5
def price_string(cents):
    """ returns a string in which the price is expressed as a combination of dollars and cents """
    d = cents // 100
    c = cents % 100
    if cents > 99:
        if c == 0:
            if d == 1:
                return str(d) + " " + "dollar"
            else: 
                return str(d) + " " + "dollars"
        elif c < 10:
            if d == 1:
                return str(d) + " " + "dollar and" + " " + str(c) + " " + "cent"
            else:
                return str(d) + " " + "dollars and" + " " + str(c) + " " + "cent"
        else:
            if d == 1:
                return str(d) + " " + "dollar and" + " " + str(c) + " " + "cents"
            else:
                return str(d) + " " + "dollars and" + " " + str(c) + " " + "cents"
    else:
        if cents < 10:
            return str(cents) + " " + "cent"
        else:
            return str(cents) + " " + "cents"
        

















        
        




