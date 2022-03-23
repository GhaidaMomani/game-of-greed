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
    def get_scorers(dice_roll):
        """
        This method it takes dice_roll as an argument ,
        and it is responsible for calculating the score by folowing the game rules.


        """

        accumulated = 0
        dice_roll = sorted(dice_roll)
        edge_case_straight = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]
        score_list = {
            (1, 1): 100,
            (1, 2): 200,
            (1, 3): 1000,
            (1, 4): 2000,
            (1, 5): 3000,
            (1, 6): 4000,
            (2, 1): 0,
            (2, 2): 0,
            (2, 3): 200,
            (2, 4): 400,
            (2, 5): 600,
            (2, 6): 800,
            (3, 2): 0,
            (3, 3): 300,
            (3, 4): 600,
            (3, 5): 900,
            (3, 6): 1200,
            (4, 2): 0,
            (4, 3): 400,
            (4, 4): 800,
            (4, 5): 1200,
            (4, 6): 1600,
            (5, 1): 50,
            (5, 2): 100,
            (5, 3): 500,
            (5, 4): 1000,
            (5, 5): 1500,
            (5, 6): 2000,
            (6, 2): 0,
            (6, 3): 600,
            (6, 4): 1200,
            (6, 5): 1800,
            (6, 6): 2400,
        }
        count = Counter(dice_roll)
        # print("before" ,count)
        count = count.most_common()
        # print("after" ,count)

        if count == edge_case_straight:
            accumulated = 1500
            return accumulated

        if len(count) == 3 and count[0][1] and count[1][1] and count[2][1] == 2:
            accumulated = 1500
            return accumulated

        for x in count:
            if x in score_list:
                accumulated += score_list[x]
                # print(accumulated)

        return accumulated

    @staticmethod
    def roll_dice(num_dice):
        """
        This method takes the number of dices as an integer argument,
         and returns a random integer for each dice between 1and 6

        """
        output = []
        # random(1, 6)
        for _ in range(num_dice):
            x = random.randint(1, 6)
            output.append(x)
            # print("me", output)

        return tuple(output)


if __name__ == "__main__":
    # from game_of_greed.banker import Banker # <--
    pass
# y = GameLogic()
# GameLogic
# print(GameLogic.calculate_score((3, 3, 3, 1, 5, 1)))
# # y.roll_dice(6)
# z = Banker()
# print(z.shelf(10))
# print(z.shelf(1100))

# print(z.shelf(1500))
# print(z.bank())
# print(z.temp_unbanked)


# all_scores = {(1, 1): 100,            (1, 2): 200,            (1, 3): 1000,            (1, 4): 2000,            (1, 5): 3000,            (1, 6): 4000,            (2, 1): 0,            (2, 2): 0,            (2, 3): 200,            (2, 4): 400,            (2, 5): 600,            (2, 6): 800,            (3, 2): 0,            (3, 3): 300,            (3, 4): 600,            (3, 5): 900,            (3, 6): 1200,            (4, 2): 0,            (4, 3): 400,            (4, 4): 800,            (4, 5): 1200,            (4, 6): 1600,            (5, 1): 50,            (5, 2): 100,            (5, 3): 500,            (5, 4): 1000,            (5, 5): 1500,            (5, 6): 2000,            (6, 2): 0,            (6, 3): 600,            (6, 4): 1200,            (6, 5): 1800,            (6, 6): 2400, }


"""
     
       first try using tuples:

       element = ((tuple(), 0),
                   ((1,), 100),
                   ((1, 1), 200),
                   ((1, 1, 1), 1000),
                   ((1, 1, 1, 1), 2000),
                   ((1, 1, 1, 1, 1), 3000),
                   ((1, 1, 1, 1, 1, 1), 4000),
                   ((2,), 0),
                   ((2, 2), 0),
                   ((2, 2, 2), 200),
                   ((2, 2, 2, 2), 400),
                   ((2, 2, 2, 2, 2), 600),
                   ((2, 2, 2, 2, 2, 2), 800),
                   ((3,), 0),
                   ((3, 3), 0),
                   ((3, 3, 3), 300),
                   ((3, 3, 3, 3), 600),
                   ((3, 3, 3, 3, 3), 900),
                   ((3, 3, 3, 3, 3, 3), 1200),
                   ((4,), 0),
                   ((4, 4), 0),
                   ((4, 4, 4), 400),
                   ((4, 4, 4, 4), 800),
                   ((4, 4, 4, 4, 4), 1200),
                   ((4, 4, 4, 4, 4, 4), 1600),
                   ((5,), 50),
                   ((5, 5), 100),
                   ((5, 5, 5), 500),
                   ((5, 5, 5, 5), 1000),
                   ((5, 5, 5, 5, 5), 1500),
                   ((5, 5, 5, 5, 5, 5), 2000),
                   ((6,), 0),
                   ((6, 6), 0),
                   ((6, 6, 6), 600),
                   ((6, 6, 6, 6), 1200),
                   ((6, 6, 6, 6, 6), 1800),
                   ((6, 6, 6, 6, 6, 6), 2400),
                   ((1, 2, 3, 4, 5, 6), 1500),
                   ((2, 2, 3, 3, 4, 6), 0),
                   ((2, 2, 3, 3, 6, 6), 1500),
                   ((1, 1, 1, 2, 2, 2), 1200))
        

        for x in range(len(element)):
            if dice_roll == element[x][0]:
                return element[x][-1]
        """
