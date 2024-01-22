def linearSearch(arr, target) -> int:
    if len(arr) == 0:
        return -1

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


def searchInString(str, target) -> bool:
    if len(str) == 0:
        return False

    for i in range(len(str)):
        if str[i] == target:
            return True

    return False


# Arr = [18,12,-7,3,14,28]
# Q. Search for 3 in the range of index [1,4]
def searchInRange(arr, searchRange, target):
    if len(arr) == 0:
        return -1

    start = searchRange[0]
    end = searchRange[1] + 1

    for i in range(start, end):
        if arr[i] == target:
            return i

    return -1


def search2DArray(arr, target):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == target:
                return [row, col]

    return -1


def maxIn2DArray(arr):
    max = arr[0][0]

    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] > max:
                max = arr[row][col]

    return max


if __name__ == "__main__":
    # arr = list(map(int, input('Please enter the array: ').split(',')))
    # target = int(input("Please enter the target: "))

    # print(linearSearch(arr, target))

    # str = input("Enter your string: ")
    # target = input("Enter the character you want to find: ")

    # print(searchInString(str, target))

    # arr = list(map(int, input('Please enter the array: ').split(',')))
    # searchRange = list(
    #     map(int, input('Please enter the starting index and ending index: ').split(',')))
    # target = int(input("Please enter the target: "))

    # print(searchInRange(arr, searchRange, target))

    twoDArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target = int(input("Please enter the target: "))

    print(search2DArray(twoDArray, target))
    print(maxIn2DArray(twoDArray))
