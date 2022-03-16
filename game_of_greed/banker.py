class Banker:
    """
    This class stores the points for each round, it banks them untill being used next
    """
    def __init__(self):  # <-
        # self.points = 0
        self.shelved = 0
        self.balance = 0
        pass

    def shelf(self, points):
        """
        input to shelf is the amount of points (integer) to add to shelf.
        """
        self.shelved += points  # <--

    def bank(self):
        """
        should add any points on the shelf to total and reset shelf to 0.
        """
        self.balance += self.shelved
        self.clear_shelf()

    def clear_shelf(self):
        """
        should remove all unbanked points.
        """
        self.shelved = 0