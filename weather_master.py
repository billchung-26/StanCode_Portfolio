"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

一開始就要把第一個值一次定義成最大、最小、平均
用if 把edge case 解決
"""
EXIT = -100

def main():
    """
    分成第一筆資料處理及後續的資料處理，第一部分先處理第一筆資料，把資料存在各個函式會用到的變數裡，
    同時處理第一個edge case，第一次就數入 -100
    第二筆後，開始用while loop 跑迴圈
    """
# --- 第一筆資料處理 ---
    data = int(input("Next Temperature: (or -100 to quit)? "))
    if data == EXIT:
        print("No temperatures were entered.")
    else:
        highest = data
        lowest = data
        total = data
        low_temp_count = 0
        low_temp_count = update_cold_days(low_temp_count, data)
        count = 1

# --- 第二筆以後的資料處理 ---

        while True:
            data = int(input("Next Temperature: (or -100 to quit)? "))
            if data == EXIT:
                break
            highest = get_new_highest(highest, data)
            lowest = get_new_lowest(lowest, data)
            total = get_total(total, data)
            low_temp_count = update_cold_days(low_temp_count, data)
            count = count + 1

        average = get_average(total, count)
        print("Highest temperature: " + str(highest))
        print("Lowest temperature: " + str(lowest))
        print("Average: " + str(average))
        print(str(low_temp_count) + " cold day(s)")


# 1. 處理最高溫的函式
def get_new_highest(current_highest, new_data):
    """
        接收目前的最高溫和新資料，回傳兩者中較大的那個
    """
    if new_data > current_highest:
        return new_data
    else:
        return current_highest

# 2. 處理最低溫的函式
def get_new_lowest(current_lowest, new_data):
    """
            接收目前的最低溫和新資料，回傳兩者中較大的那個
    """
    if new_data < current_lowest:
        return new_data
    else:
        return current_lowest

# 3. 處理平均溫度之前算溫度總和的函式
def get_total(current_total, new_data):
    current_total = current_total + new_data
    return current_total

# 4. 處理平均溫度之前算溫度總和的函式
def get_average(total, count):
    if count == 0:
        return 0
    else:
        return total/count

# 5. 處理低溫天數的函式
def update_cold_days(low_count, new_data):
    if new_data < 16:
        low_count = low_count + 1
    return low_count

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
