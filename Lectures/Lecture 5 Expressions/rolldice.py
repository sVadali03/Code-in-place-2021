"""
Simulate rolling two dice.
Prints results of each roll as well as the total.
"""

import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # setting seed is useful for debugging
    #random.seed(3)
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()
