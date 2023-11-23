# finalproject.py (Final Project, Part 1)
#
# Building an initial text model
#  

def clean_text(txt):
    """ takes a string of text txt as a parameter and returns a list 
            containing the words in txt after it has been “cleaned”.
    """
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('?', '')
    txt = txt.replace('!', '')
    txt = txt.replace(';', '')
    txt = txt.replace(':', '')
    txt = txt.replace('"', '')
    txt = txt.replace('?', '')
    txt = txt.lower()
    txt = txt.split(' ')
    return txt
    
def stem(s):
    """ return the root part of the word of s. """
    if s[-2:] == 'es':
        stem_rest = stem(s[:-2])
        return stem_rest
    elif s[-1:] == 's':
        stem_rest = stem(s[:-1])
        return stem_rest
    elif s[-2:] == 'er' or s[-2:] == 'or' or s[-2:] == 'ar':
        stem_rest = stem(s[:-2])
        return stem_rest
    elif s[-4:] == 'tion' or s[-4:] == 'hood' or s[-4:] == 'ship':
        stem_rest = stem(s[:-4])
        return stem_rest
    elif s[-2:] == 'ly':
        stem_rest = stem(s[:-2])
        return stem_rest
    elif s[-3:] == 'ing':
        stem_rest = stem(s[:-3])
        return stem_rest
    elif s[-3:] == 'ize' or s[-3:] == 'ify':
        stem_rest = stem(s[:-3])
        return stem_rest
    elif s[-2:] == 'ed':
        stem_rest = stem(s[:-2])
        return stem_rest
    elif s[-3:] == 'ful' or s[-3:] == 'ish' or s[-3:] == 'ive':
        stem_rest = stem(s[:-3])
        return stem_rest
    elif s[-2:] == 'al':
        stem_rest = stem(s[:-2])
        return stem_rest
    elif s[-2:] == 'ty' or s[-2:] == 'dy':
        stem_rest = s[:-1]
        stem_rest += 'i'
        return stem_rest
    elif s[-2:] == 've':
        stem_rest = s[:-1]
        return stem_rest
    elif s[:2] == 'un' or s[:2] == 'in' or s[:2] == 'ir':
        stem_rest = stem(s[2:])
        return stem_rest
    elif s[:3] == 'mis' or s[:3] == 'non' or s[:3] == 'pre' or s[:3] == 'pro' or s[:3] == 'dis':
        stem_rest = stem(s[3:])
        return stem_rest
    elif s[:4] == 'anti' or s[:4] == 'auto' or s[:4] == 'mini' or s[:4] == 'fore':
        stem_rest = stem(s[4:])
        return stem_rest
    elif s[:5] == 'trans' or s[:5] == 'inter' or s[:5] == 'super' or s[:5] == 'under':
        stem_rest = stem(s[5:])
        return stem_rest
    else:
        return s
    
def clean_stem(txt):
    result = []
    word_list = clean_text(txt)
    for w in word_list:
        result += [stem(w)]
    return result
    
def clean_words(txt):
    """ takes a string of text txt as a parameter and returns a list 
            containing the punctuations in txt after it has been “cleaned”.
    """
    txt = txt.lower()
    txt = txt.replace('a', '')
    txt = txt.replace('b', '')
    txt = txt.replace('c', '')
    txt = txt.replace('d', '')
    txt = txt.replace('e', '')
    txt = txt.replace('f', '')
    txt = txt.replace('g', '')
    txt = txt.replace('h', '')
    txt = txt.replace('i', '')
    txt = txt.replace('j', '')
    txt = txt.replace('k', '')
    txt = txt.replace('l', '')
    txt = txt.replace('m', '')
    txt = txt.replace('n', '')
    txt = txt.replace('o', '')
    txt = txt.replace('p', '')
    txt = txt.replace('q', '')
    txt = txt.replace('r', '')
    txt = txt.replace('s', '')
    txt = txt.replace('t', '')
    txt = txt.replace('u', '')
    txt = txt.replace('v', '')
    txt = txt.replace('w', '')
    txt = txt.replace('x', '')
    txt = txt.replace('y', '')
    txt = txt.replace('z', '')
    txt = txt.replace(' ', '')
    return txt

def split_sentence(txt):
    txt = txt[:-1]
    txt = txt.split('. ' or '? ' or '! ')
    return txt



class TextModel:
    def __init__(self, model_name):
        """ constructs a new TextModel object by accepting a string model_name 
            as a parameter
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}
        
    def __repr__(self):
        """ Return a string representation of the TextModel. """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) +'\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuation)) + '\n'
        return s
    
    def add_string(self, s):
        """ Analyzes the string txt and adds its pieces to all of the 
            dictionaries in this text model.
        """
        sentence_list = split_sentence(s)
        for w in sentence_list:
            w = w.split(' ')
            if len(w) not in self.sentence_lengths:
                self.sentence_lengths[len(w)] = 1
            else:
                self.sentence_lengths[len(w)] += 1
                
        punctuation_list = clean_words(s)
        for w in punctuation_list:
            if w not in self.punctuation:
                self.punctuation[w] = 1
            else:
                self.punctuation[w] += 1
                
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
        for w in word_list:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
                
        stem_list = clean_stem(s)
        for w in stem_list:
            if w not in self.stems:
                self.stems[w] = 1
            else:
                self.stems[w] += 1
        
                
    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the 
            model.
        """
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        txt = file.read()
        file.close()
        self.add_string(txt)
        
    def save_model(self):
        """ saves the TextModel object self by writing its various feature
            dictionaries to files.
        """
        d1 = self.words
        JKR_words = open('JKR_words', 'w')
        JKR_words.write(str(d1))
        JKR_words.close()
        
        d2 = self.word_lengths
        JKR_word_lengths = open('JKR_word_lengths', 'w')
        JKR_word_lengths.write(str(d2))
        JKR_word_lengths.close()

        d3 = self.stems
        JKR_stems = open('JKR_stems', 'w')
        JKR_stems.write(str(d3))
        JKR_stems.close()
        
        d4 = self.sentence_lengths
        JKR_sentence_lengths = open('JKR_sentence_lengths', 'w')
        JKR_sentence_lengths.write(str(d4))
        JKR_sentence_lengths.close()
        
        d5 = self.punctuation
        JKR_punctuation = open('JKR_punctuation', 'w')
        JKR_punctuation.write(str(d5))
        JKR_punctuation.close()

    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object 
            from their files and assigns them to the attributes of the called 
            TextModel.
        """
        JKR_words = open('JKR_words', 'r')
        JKR_words_str = JKR_words.read()
        JKR_words.close()
        self.words = dict(eval(JKR_words_str))

        JKR_word_lengths = open('JKR_word_lengths', 'r')
        JKR_word_lengths_str = JKR_word_lengths.read()
        JKR_word_lengths.close()
        self.word_lengths = dict(eval(JKR_word_lengths_str))
        
        JKR_stems = open('JKR_stems', 'r')
        JKR_stems_str = JKR_stems.read()
        JKR_stems.close()
        self.stems = dict(eval(JKR_stems_str))
        
        JKR_sentence_lengths = open('JKR_sentence_lengths', 'r')
        JKR_sentence_lengths_str = JKR_sentence_lengths.read()
        JKR_sentence_lengths.close()
        self.sentence_lengths = dict(eval(JKR_sentence_lengths_str))

        JKR_punctuation = open('JKR_punctuation', 'r')
        JKR_punctuation_str = JKR_punctuation.read()
        JKR_punctuation.close()
        self.punctuation = dict(eval(JKR_punctuation_str))
     
    def similarity_scores(self, other):
        """ returns a list of log similarity scores measuring the similarity
            of self and other.
        """
        result = []
        result += [compare_dictionaries(other.words, self.words)]
        result += [compare_dictionaries(other.word_lengths, self.word_lengths)]
        result += [compare_dictionaries(other.stems, self.stems)]
        result += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        result += [compare_dictionaries(other.punctuation, self.punctuation)]
        return result
    
    def classify(self, source1, source2):
        """ compares the called TextModel object (self) to two other “source”
            TextModel objects (source1 and source2) and determines which of 
            these other TextModels is the more likely source of the called 
            TextModel.
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        weighted_sum1 = 10 * scores1[0] + 5 * scores1[1] + 7 * scores1[2] + 5 * scores1[3] + 3 * scores1[4]
        weighted_sum2 = 10 * scores2[0] + 5 * scores2[1] + 7 * scores2[2] + 5 * scores2[3] + 3 * scores2[4]
        print('scores for source1: ' + str(scores1))
        print('scores for source2: ' + str(scores2))
        if weighted_sum1 > weighted_sum2:
            print(str(self.name) + ' is more likely to have come from ' + str(source1.name))
        if weighted_sum1 < weighted_sum2:
            print(str(self.name) + ' is more likely to have come from ' + str(source2.name))
        
        

def compare_dictionaries(d1, d2):
    """  take two feature dictionaries d1 and d2 as inputs, and it should 
        compute and return their log similarity score.
    """
    import math
    score = 0
    total = 0
    for w in d1:
        total += d1[w]
    for x in d2:
        if x in d1:
            score += math.log(d1[x] / total) * d2[x]
        else:
            score += math.log(0.5 / total) * d2[x]
    return score


        
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)  

               
        
def run_tests():
    """ your docstring goes here """
    Brave_New_World = TextModel('Brave_New_World')
    Brave_New_World.add_file('Brave_New_World.txt')

    Walden = TextModel('Walden')
    Walden.add_file('Walden.txt')

    new1 = TextModel('1984')
    new1.add_file('1984.txt')
    new1.classify(Brave_New_World, Walden)        
        
    new2 = TextModel('The_Moon_and_Sixpence')
    new2.add_file('The_Moon_and_Sixpence.txt')
    new2.classify(Brave_New_World, Walden) 
        
    new3 = TextModel('Wuthering_Heights')
    new3.add_file('Wuthering_Heights.txt')
    new3.classify(Brave_New_World, Walden) 
        
    new4 = TextModel('The_Old_Man_and_the_Sea')
    new4.add_file('The_Old_Man_and_the_Sea.txt')
    new4.classify(Brave_New_World, Walden)    
        
        
        

        
        