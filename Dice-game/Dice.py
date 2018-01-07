import random

class Dice(object):
    def __init__(self):
        self.right = random.choice([6, 12])
        if self.right == 12:
            self.left = 6
        else:
            self.left = 12
        self.left_count, self.right_count = [], []
        for i in range(1, self.left + 1):
            self.left_count.append({i : 0})
        for i in range(1, self.right + 1):
            self.right_count.append({i : 0})
        self.right = "right"
        self.left = "left"

class Game(Dice):
    def __init__(self):
        super().__init__()
        self.hand = ""
        self.left_prob = 0.5
        self.right_prob = 0.5
        self.trues = 0
        self.rolls = 0
        print("\nLeft hand Probability: 50%\n")
        print("Right hand Probability: 50%\n")
        self.menu()

    def roll(self):
        self.trues = 0
        self.hand = input("Please choose which hand to roll: ")
        while not (self.hand == "left") or (self.hand == "right"):
            self.hand = input("\n\nPlease choose which hand to roll: ")
        self.rolls = int(input("\nNumber of rolls: ")) + 1
        for i in range(1, self.rolls):
            if (self.hand == self.left):
                rand = random.randint(1, len(self.left_count))
                self.left_count[rand - 1][rand] += 1
            else:
                rand = random.randint(1, len(self.right_count))
                self.right_count[rand - 1][rand] += 1
            if rand >= 4:
                print("Roll %d: True" %  i, end="\t")
                self.trues += 1
            else:
                print("Roll %d: False" %  i, end="\t")

            if i % 5 == 0:
              print("\n")
        self.stats()

    def stats(self):
        print("Current statistics: ")
        print("\nLeft hand Probability: \n")
        if self.hand == "left":
            self.left_prob = self.trues / self.rolls
            print(self.left_prob)
        print("Right hand Probability: \n")
        if self.hand == "right":
            self.right_prob = self.trues / self.rolls
            print(self.right_prob)

    def guess(self):
        choice = input("\nEnter guess: left or right?\n")
        if (choice == "left" and len(self.left_count) == 12) or (choice == "right" and len(self.right_count) == 12):
            print("\nYOU WIN!\n")
        else:
            print("YOU LOSE!\n")
        print("Left hand Statistics: \n")
        for i in range(len(self.left_count)):
            final_left = self.left_count[i][i + 1]
            print("%d's: %d" % (i + 1, final_left))
            print(final_left * "*")
        print("\nRight hand Statistics: \n")
        for i in range(len(self.right_count)):
            final_right = self.right_count[i][i + 1]
            print("%d's: %d" % (i + 1, final_right))
            print(final_right * "*")

    def menu(self):
        option = input("""Menu:
        1 = Roll the dice!

        2 = Look at roll statistics

        3 = Guess which hand

        Enter selection: """)
        while option != "q":
            if option == "1":
                self.roll()
            if option == "2":
                self.stats()
            if option == "3":
                self.guess()
            option = input("""Menu:
            1 = Roll the dice!

            2 = Look at roll statistics

            3 = Guess which hand

            Enter selection: """)

game = Game()
