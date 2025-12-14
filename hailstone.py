"""
File: hailstone.py
Name: Bill
-----------------------
Douglas Hofstadter 獲得普立茲獎的得獎著作 《Gödel, Escher, Bach》裡⾯有許多有趣的數學謎題（很多問題都可以⽤電腦程式來計算）。
在書中，Hofstadter 提到，選⼀正整數 n ，重複以下指令，直到 n 變成 1：
•如果 n 是奇數，把 n 乘 3 再加 1
•如果 n 是偶數，對 n 除 2
現在請同學寫出⼀個程式，可以讓使⽤者輸入任意整數，並產⽣ Hailstone Sequence。
如書中的圖例，所有在抵達 1 之前的數字都會被列舉出來。
同時，這個序列中從 n 到 1 之間運算的次數 ( steps ) 也會被紀錄。
"""

"""
Methods:



"""


def main():
    """

    """
    print('Input your magic number:')
    print('')
    guess = int(input('Your Magic Number: '))
    trial = 0
    initial = 0

    while guess != 1:
        if guess % 2 == 0:
            initial = guess
            guess //= 2
            print(str(initial) + ' is even, so I take half: ' + str(guess))
            trial += 1
        else:
            initial = guess
            guess = guess*3 + 1
            print(str(initial) + ' is odd, so I make 3n+1: '+ str(guess))
            trial += 1
    print('It took ' + str(trial) + ' steps to reach 1')

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
