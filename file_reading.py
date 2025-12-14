"""
File: file_reading.py
—————————————————————————————————
This program reads input from a file named “data.txt” and 
processes each line to extract all numerical digits. 
After collecting the digits, the program calculates and 
displays the maximum, minimum, and average values on the console.
"""


FILE = 'data.txt'
FILE1 = 'data_1.txt'


def main():
    minimum = float ("inf")
    maximum = -float ("inf")
    count = 0
    total = 0
    f = open("data.txt", 'r')
    print(f.read())

    for line in f:
        if line != "Nan\n":
            data = float(line)
            if data > maximum:
                maximum = data
            if data < minimum:
                minimum = data
            total += data
            count += 1
    f.close()
    if count == 0:
        print("no data")
    else:
        print('max:' + str(maximum))
        print('min:' + str(minimum))
        print('avg:' + str(total/count))







if __name__ == '__main__':
    main()
