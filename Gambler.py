import random


class Gambler:

    def __init__(self, start_amount, goal_amount):  # initialize constructor using parameter
        self.start_amount = start_amount
        self.goal_amount = goal_amount

    def calculate_average_count(self):  # define method for calculate percentage of loss and wins

        count_bet = 0
        win_count = 0
        loss_count = 0

        while True:

            if self.start_amount == 0 or self.start_amount == self.goal_amount:
                break

            else:
                random_value = int(random.choice([0, 1]))
                count_bet = count_bet + 1

                if random_value == 1:
                    self.start_amount = self.start_amount + 1
                    win_count = win_count + 1

                else:
                    self.start_amount = self.start_amount - 1
                    loss_count = loss_count + 1

        return win_count, loss_count, count_bet


while True:

    try:

        stake_value = int(input("Enter the start amount : "))

        if stake_value < 0:
            print("Please Enter Positive Value")
            continue

        goal_value = int(input("Enter goal amount you want : "))

        if goal_value < 0:
            print("Please Enter Positive Value")
            continue

        gambler_object = Gambler(stake_value, goal_value)

        winCount, lossCount, countBet = gambler_object.calculate_average_count()

        print("Percentage of win : ", (winCount / countBet) * 100)
        print("Percentage of loss : ", (lossCount / countBet) * 100)
        break

    except ValueError:
        print("Please Enter Digit Value")

    except:
        print("Exception Occured ")