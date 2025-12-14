"""
File: hangman.py
Name:Bill
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random
import string

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    先設定example 為隨機題目，current_dash 為該題目的dash版本，也是玩家要填空的目標
    """
    example = random_word()
    current_dash = set_up(example)
    # 1. 設置一個可變變數來追蹤剩餘次數
    remaining_turns = N_TURNS
    print("\n--- Game Start ---")
    # 2. 遊戲循環：只要還有猜測次數 AND 虛線單字還沒完全猜對
    while remaining_turns > 0 and current_dash != example:
    # 每次進入迴圈時，先顯示當前狀態
        print("\nThe word looks like: " + current_dash)
        print("You have " + str(remaining_turns) + " guesses left.")
        guess_input = str(input('Your guess: '))
    # 3. 呼叫函式並接收【兩個】回傳值：更新後的單字狀態 和 更新後的剩餘次數
        current_dash, remaining_turns = verify_guess(guess_input, example, current_dash, remaining_turns)
    # 4. 迴圈結束，判斷勝負
    if current_dash == example:
        print("\n--- 恭喜！您猜中了！---")
        print("The word was: " + example)
    else:  # remaining_turns <= 0
        print("\n--- 挑戰失敗！---")
        print("You ran out of guesses! The word was: " + example)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"

def set_up(string):
    # 最一開始設定為七個dash
    ans = ''
    for i in range(len(string)):
        ans = ans +'-'
    return ans

def verify_guess(guess, example, current_dash, remaining_turns):
    # 確保猜測字母是大寫
    verify_alpha = guess.isalpha()
    if  verify_alpha and len(guess) ==1:
        guess = guess.upper()
        # 建立一個新的字串來存放更新後的結果。一開始它就是原本的 dash
        new_dash = current_dash
        #初始化旗標：假設一開始字母沒有被找到
        found = False

        for i in range(len(example)):
            if guess == example[i]:
                # 1. 取得 i 之前的所有字元 (例如：如果 i=2，取得 dash[0] 和 dash[1])
                left_part = new_dash[0:i]
                # 2. 取得 i 之後的所有字元 (例如：如果 i=2，取得 dash[3] 到結尾)
                # 因為 example[i] 和 guess 已經是正確的字母，所以我們用 example[i] 來替換
                right_part = new_dash[i + 1:]
                # 3. 將左邊部分、正確字母、右邊部分拼接起來，並重新賦值給 new_dash
                # 完成「替換」
                new_dash = left_part + example[i] + right_part
                # 🚩 找到字母了！將旗標設為 True
                found = True
        if not found:
            print("There is no " + guess + "'s in the word.")
            # 減少剩餘次數
            remaining_turns -= 1

        return new_dash, remaining_turns
    else:
        print("Illegal format.")
        return current_dash, remaining_turns


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
"""
verify_guess(guess, example, dash)
    print(verify_guess)
    跟
guess = verify_guess(guess, example, dash)
    print(guess)
有什麼差別？
"""