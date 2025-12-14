"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
    """
    要讓程式一直跑，做不只一次check, 因此我們首先使用while true
    再來先檢查輸入的數字是否有match exit，如果有的話先break
    後面檢查質數，我們先假設狀況為等於質數，再來檢查輸入的數字是否為非質數，跑for loop 要從2開始跑，因為0跟1都不能先除以我們輸入的數字，會導致錯誤
    """
while True:
    print("Welcome to the prime checker!")
    data = int(input("n:"))
    if data == EXIT:
        print("Have a good day!")
        break
    else:
        is_prime = True
        for i in range (2, data):
            if data % i == 0:
                is_prime = False
                break
        if is_prime:
            print(str(data) + " is a prime number")
        else:
            print(str(data) + " is not a prime number")

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
