"""
File: python_random_generator.py
Name: 
———————————————————————————————————
This program simulates a certain number of die-roll results and calculates
how many consecutive number (defined as runs) appears.
"""


import random


NUM_ROLLS = 15


def main():
    # Your code here
    can_add = True
    run =0
    old_roll = random.randrange(1,7)
    for i in range(NUM_ROLLS-1):
        new_roll = random.randrange(1,7)
        if old_roll == new_roll:
            if can_add:
                run += 1
                can_add = False
        else:
            can_add = True
        old_roll = new_roll





if __name__ == '__main__':
    main()
