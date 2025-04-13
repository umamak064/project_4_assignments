"""
Program: dicesimulator
----------------------
Simulates rolling two dice, three times.
Demonstrates how variable scope works in Python.
"""

import random

# Each die has 6 sides
NUM_SIDES = 6

def roll_dice():
    """
    Rolls two dice and prints the total.
    These variables exist only inside this function.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    # This die1 is in a different scope from the one in roll_dice
    die1 = 10
    print("die1 in main() starts as:", die1)

    # Simulate three rolls
    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() is still:", die1)

# Required to run the main function
if __name__ == '__main__':
    main()
