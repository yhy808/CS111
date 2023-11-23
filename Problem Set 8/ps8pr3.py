#
# ps8pr3.py  (Problem Set 8, Problem 3)
#
# Markov text generation    
#

def create_dictionary(filename):
    """ takes a string representing the name of a text file, and that 
        returns a dictionary of key-value pairs. 
    """
    file = open(filename, 'r')
    text = file.read()      
    file.close()
    words = text.split()
    
    d = {}
    current_word = '$'
    
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
            if next_word[-1] == '.' or next_word[-1] == '!' or next_word[-1] == '?':
                current_word = '$'
            else:
                current_word = next_word
        else:
            d[current_word] += [next_word]
            if next_word[-1] == '.' or next_word[-1] == '!' or next_word[-1] == '?':
                current_word = '$'
            else:
                current_word = next_word
    return d

def generate_text(word_dict, num_words):
    """ takes as parameters a dictionary of word transitions (generated 
        by the create_dictionary function) named word_dict and a positive 
        integer named num_words. The function must use word_dict to 
        generate and print num_words words, with a space after each word.
    """
    import random
    current_word = '$'
    for x in range(num_words):
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end = ' ')
        if next_word[-1] == '.' or next_word[-1] == '!' or next_word[-1] == '?':
            current_word = '$'
        else:
            current_word = next_word
    print()
        
        




























