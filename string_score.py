"""
File: string_score.py
Name:
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    # digit->1 ; upper->2; lower->3
    """

    print(score('1aB4rC')) # 12
    print(score('aaaaA3'))
    # 15


def score(string):
    """
    :param dna: str+integer
    :return: calculation of the score, which is an integer

    """
    user_score = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            user_score += 1
        elif ch.isupper():
            user_score += 2
        elif ch.islower():
            user_score += 3
        else:
            user_score += 0
    return user_score




if __name__ == '__main__':
    main()