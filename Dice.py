"""
This program draws histogram statistics of the number of times a dice lands on each number of a
six sided dice. The user inputs the amount of thows desired and each outcome as well as the final
histogram is displayed in the output.

* Enter a number of rolls greate than 300 to produce a better histogram.
"""

import random

max_num = 6
rolls = int(input("Number of rolls: ")) + 1 

count = [
    ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"],
    [{1 : 0}, {2 : 0}, {3 : 0}, {4 : 0}, {5 : 0},{6 : 0}]
]

# Generate random value, add to tally in count, print roll info
for i in range(1, rolls):
    rand = random.randint(1, max_num)
    count[1][rand - 1][rand] += 1
    print("Roll %d: %d" %  (i, rand), end="\t")
    if i % 5 == 0:
      print("\n")

print("\n")

# Output
for i in range(max_num):
    final_count = count[1][i][i + 1]
    print("%s: %d" % (count[0][i], final_count))
    print(final_count * "*")
