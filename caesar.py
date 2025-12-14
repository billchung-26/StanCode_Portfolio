"""
File: caesar.py
Name:Bill
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    let customers to input secret number and password
    pass password and secret number to ciphered
    """
    secret = int(input('Secret number: '))
    password = input('Password: ')
    ans = ciphered(password, secret)

    print(ans)

def ciphered(password, secret):
    """
        first, we have all the password input to be capitalized
        second, we check if the password is alphabet
        then,we find the location of that character
        and, we have a whole_string to have the whole string to be the new reference
        last, we use the location to lookup for the new whole string
    """
    ans = ''
    password = password.upper()
    for i in range(len(password)):
        if password[i].isalpha():
            location = ALPHABET.find(password[i])
            back_string = ALPHABET[0:secret]
            front_string = ALPHABET[secret:26]
            whole_string = front_string + back_string
            ans += whole_string[location]
        else:
            ans += " "

    return ans



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
