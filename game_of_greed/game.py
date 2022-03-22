# add game_of_greed."" if you want to run file not pytest!
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from typing import Counter


class Game:
    def __init__(self, roller=None, dice_roll_score=None):
        self.roller = roller or GameLogic.roll_dice
        self.dice_roll_score = dice_roll_score
        self.banker = Banker()

    def play(self):

        self.banker.clear_shelf()

        numof_rolled_dice = 6
        round_count = 1
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")

        else:

            choice_message = "Enter dice to keep (no spaces), or (q)uit: "
            round_message = f"Starting round {round_count}"
            print(round_message)
            rolled_dice = self.roller(numof_rolled_dice)
            print(f"Rolling {numof_rolled_dice} dice...")

            nums = []

            for i in rolled_dice:
                nums.append(str(i))
            print(",".join(nums))

            while True:

                self.dice_roll_score = tuple(int(x) for x in nums)
                checker = Counter(self.dice_roll_score).most_common()

                score_decision = GameLogic.calculate_score(self.dice_roll_score)

                if score_decision == 0:
                    print("Zilch!!! Round over")
                    print(
                        f"You banked 0 points in round {round_count}\nTotal score is 0 points"
                    )
                    self.banker.clear_shelf()
                    round_count += 1
                    round_message = f"Starting round {round_count}"
                    print(round_message)
                    numof_rolled_dice = 6
                    rolled_dice = self.roller(numof_rolled_dice)

                    print(f"Rolling {numof_rolled_dice} dice...")

                    nums = []
                    for i in rolled_dice:
                        nums.append(str(i))

                    print(",".join(nums))

                else:

                    decision = input(choice_message)

                    if decision == "q":
                        anti_cheat = False

                        if (
                            self.banker.balance == 0
                            and round_count == 1
                            and anti_cheat == False
                        ):
                            print("Thanks for playing. You earned 0 points")

                        else:
                            print(f"Total score is {self.banker.balance} points")
                            print(
                                f"Thanks for playing. You earned {self.banker.balance} points"
                            )
                            self.banker.clear_shelf()
                        break

                    elif decision == "b":

                        shelfed = self.banker.shelved
                        self.banker.bank()
                        print(f"You banked {shelfed} points in round {round_count}")

                        print(f"Total score is {self.banker.balance} points")
                        choice_message = "Enter dice to keep (no spaces), or (q)uit: "

                        round_count += 1
                        round_message = f"Starting round {round_count}"
                        print(round_message)

                        numof_rolled_dice = 6
                        rolled_dice = self.roller(numof_rolled_dice)

                        print(f"Rolling {numof_rolled_dice} dice...")
                        nums = []
                        for i in rolled_dice:
                            nums.append(str(i))
                        print(",".join(nums))

                    elif decision == "r":
                        choice_message = "Enter dice to keep (no spaces), or (q)uit: "
                        rolled_dice = self.roller(numof_rolled_dice)

                        print(f"Rolling {numof_rolled_dice} dice...")
                        nums = []
                        for i in rolled_dice:
                            nums.append(str(i))
                        print(",".join(nums))
                        if numof_rolled_dice == 0:
                            numof_rolled_dice = 6

                    else:
                        before_decision = decision
                        before_decision = ",".join(before_decision)
                        decision = tuple(int(x) for x in decision)
                        self.dice_roll_score = decision

                        new_nums = []
                        for i in nums:
                            new_nums.append(int(i))

                        y = Counter(new_nums).most_common()

                        checker = Counter(self.dice_roll_score).most_common()

                        anti_cheat = False
                        for i in range(0, len(y)):

                            if y[i][0] == checker[0][0]:

                                if y[i][1] >= checker[0][1]:
                                    anti_cheat = True

                        if anti_cheat == False:
                            print("Cheater!!! Or possibly made a typo...")
                            print(",".join(nums))
                            round_count += 1
                            continue

                        numof_rolled_dice = numof_rolled_dice - len(decision)

                        score_decision = GameLogic.calculate_score(self.dice_roll_score)

                        self.banker.shelf(score_decision)
                        print(
                            f"You have {self.banker.shelved} unbanked points and {numof_rolled_dice} dice remaining"
                        )
                        choice_message = "(r)oll again, (b)ank your points or (q)uit "

                        if numof_rolled_dice == 0:
                            numof_rolled_dice = 6


if __name__ == "__main__":

    from game_logic import GameLogic

    game = Game(GameLogic.roll_dice, GameLogic.calculate_score)

    game.play()
