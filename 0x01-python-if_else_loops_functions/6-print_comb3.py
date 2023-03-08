#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(10):
        if first_num < second_num and first_num != second_num:
            if first_num != 8:
                print("{:d}{:d},".format(first_num, second_num), end=" ")
print(89)
