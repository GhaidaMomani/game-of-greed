from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self, roller=None, dice_roll_score=None):
        self.roller = roller  # or GameLogic.roll_dice
        self.dice_roll_score = dice_roll_score
        self.banker = Banker()

    def play(self):
        # self.current_decision_score = 0
        # self.current_unbanked_score = 0
        # self.total_banked_score = 0
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

                # choice_2 = "Enter dice to keep (no spaces), or (q)uit:"

                # print(*rolled_dice, sep=',')
                decision = input(choice_message)

                if decision == "q":

                    if self.banker.balance == 0:
                        print("Thanks for playing. You earned 0 points")
                    # print(
                    #     f"Thanks for playing. You earned {self.total_banked_score}  points"
                    # )
                    else:
                        print(f"Total score is {self.banker.balance} points")
                        print(
                            f"Thanks for playing. You earned {self.banker.balance} points"
                        )
                        self.banker.clear_shelf()
                    break

                elif decision == "b":

                    # self.x = GameLogic.calculate_score(self.dice_roll_score)
                    # print(
                    #     f"You banked {self.current_unbanked_score} points in round {round_count} "
                    # )
                    shelfed = self.banker.shelved
                    self.banker.bank()
                    print(f"You banked {shelfed} points in round {round_count}")
                    # self.total_banked_score += self.current_decision_score

                    print(f"Total score is {self.banker.balance} points")
                    choice_message = "Enter dice to keep (no spaces), or (q)uit: "
                    # print("check_tuple########", decision)
                    round_count += 1
                    round_message = f"Starting round {round_count}"
                    print(round_message)
                    # self.current_decision_score = 0
                    # self.current_unbanked_score = 0

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

                    decision = tuple(int(x) for x in decision)
                    self.dice_roll_score = decision
                    # self.current_decision_score += GameLogic.calculate_score(
                    #     self.dice_roll_score
                    # )
                    numof_rolled_dice = numof_rolled_dice - len(decision)
                    # self.total_banked_score += self.current_decision_score
                    # self.current_unbanked_score += self.current_decision_score
                    score_decision = GameLogic.calculate_score(self.dice_roll_score)
                    self.banker.shelf(score_decision)
                    print(
                        f"You have {self.banker.shelved} unbanked points and {numof_rolled_dice} dice remaining"
                    )
                    choice_message = "(r)oll again, (b)ank your points or (q)uit "
                    # self.current_decision_score = 0

                    # print("check_tuple########", decision)
                    if numof_rolled_dice == 0:
                        numof_rolled_dice = 6


if __name__ == "__main__":

    from game_logic import GameLogic

    game = Game(GameLogic.roll_dice, GameLogic.calculate_score)

    game.play()
