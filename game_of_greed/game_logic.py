import random
from typing import Counter

class GameLogic:
    """
   This class will handle backend logic of the game 
    which contains two methods : calculate score and roll_dice

    """
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(dice_roll):
        """
        This method it takes dice_roll as an argument , 
        and it is responsible for calculating the score by folowing the game rules.
        

        """
        accumulated = 0
        dice_roll = sorted(dice_roll)
        edge_case_straight =  [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]
        score_list = {(1, 1): 100, (1, 2): 200, (1, 3): 1000, (1, 4): 2000, (1, 5): 3000, (1, 6): 4000, (2, 1): 0, (2, 2): 0, (2, 3): 200, (2, 4): 400, (2, 5): 600, (2, 6): 800, (3, 2): 0, (3, 3): 300, (3, 4): 600, (3, 5): 900, (3, 6): 1200, (4, 2): 0, (4, 3): 400, (4, 4): 800, (4, 5): 1200, (4, 6): 1600, (5, 1): 50, (5, 2): 100, (5, 3): 500, (5, 4): 1000, (5, 5): 1500, (5, 6): 2000, (6, 2): 0, (6, 3): 600, (6, 4): 1200, (6, 5): 1800, (6, 6): 2400,
                      }
        count = Counter(dice_roll)
        #print("before" ,count)
        count= count.most_common()
        #print("after" ,count)
        
        if count == edge_case_straight:
            accumulated = 1500
            return accumulated

        if len(count) == 3 and count[0][1] and count[1][1] and count[2][1] == 2 :
            accumulated = 1500
            return accumulated          

        
        for x in count:
            if x in score_list:
                accumulated += score_list[x]
                #print(accumulated)
          
        return accumulated


        
     