"""
File: quadratic_solver.py
Name: Bill
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    we have a if expression to identify the 3 situations of the root:
    first expression: check if b * b - 4 * a * c = 0, if yes, it's one root, and we will print that root
    second expression: check if b * b - 4 * a * c > 0, if yes, it's two roots, and we will print both roots
    third expression: else it means b * b - 4 * a * c < 0,  we will print no roots
    """
    print('This is your stanCode Quadratic Solver!, please input your number!')
    a = int(input('Enter Number a: '))
    b = int(input('Enter Number b: '))
    c = int(input('Enter Number c: '))
    if b * b - 4 * a * c == 0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        print('One root: =' + str(x1))
    elif b * b - 4 * a * c > 0:
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x3 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        print('Two roots: =' + str(x2) + ' and ' + str(x3))
    else:
        print('No real roots!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
