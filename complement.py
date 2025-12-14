"""
File: complement.py
Name: Bill
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    we make sure that the complement of each ATCG is completed by using for to check all letter, and if to check each scenario
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
        :param dna: str
        :return: str, the complement of dna, if no dna, we return dna strand is missing.
    """

    ans = ''
    if len(dna) == 0:
        return 'DNA strand is missing.'
    else:
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans += 'T'
            elif ch == 'T':
                ans += 'A'
            elif ch == 'C':
                ans += 'G'
            else:
                ans += 'C'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
