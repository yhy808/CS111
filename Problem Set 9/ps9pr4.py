#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object. """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object. """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the
            board, and that returns the index of the column with the maximum 
            score. 
        """
        self.scores = scores
        m = scores[0]
        result = [0]
        for i in range(1, len(scores)):
            if m < scores[i]:
                m = scores[i]
                result = [i]
            elif m == scores[i]:
                m = scores[i]
                result += [i]
        if self.tiebreak == 'LEFT':
            return result[0]
        elif self.tiebreak == 'RIGHT':
            return result[-1]
        else:
            return random.choice(result)
    
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s 
            scores for the columns in b.
        """
        scores = [50] * b.width
        m = self.checker
        n = self.opponent_checker()
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(m) == True:
                scores[col] = 100
            elif b.is_win_for(n) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(m, col)
                opponent = AIPlayer(n, self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                elif max(opp_scores) == -1:
                    scores[col] = -1
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move. """
        scores = self.scores_for(b)
        return self.max_score_column(scores)
    
    
    
    
    
    
    
    
    
    
    