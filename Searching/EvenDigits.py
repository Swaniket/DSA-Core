# Given an array nums of integers, return how many of them contain an even number of digits.
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
import math


def checkEven(nums):
    count = 0
    for num in nums:
        if num < 0:
            num = num * -1
        if (hasEvenDigits3(num)):
            count = count + 1
    return count


def hasEvenDigits(num):
    numberOfDigits = 0
    while (num > 0):
        numberOfDigits = numberOfDigits + 1
        num = num / 10

    if (numberOfDigits % 2 == 0):
        return True
    return False


def hasEvenDigits2(num):
    numStr = str(num)
    if (len(numStr) % 2 == 0):
        return True
    return False


def hasEvenDigits3(num):
    digits = int(math.log10(num)) + 1
    return digits % 2 == 0


if __name__ == '__main__':
    nums = list(map(int, input('Enter the array: ').split(',')))
    print(checkEven(nums))
