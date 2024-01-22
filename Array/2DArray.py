# Lets consider an example where it captures the temp 4 times a day
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

# We will use numpy as it supports 2D array perfectly
import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5],
                     [12, 17, 12, 8], [15, 18, 14, 9]])
# print(twoDArray)


# Value Insersion - It can be done in 2 way - Adding Column and Adding Row
# axis=1 -> Column | axis=0 -> Row
newTwoDArray = np.insert(twoDArray, 2, [[1, 2, 3, 4]], axis=1)
newTwoDArray = np.insert(twoDArray, -1, [[5, 6, 7, 8]], axis=0)

newTwoDArray = np.append(twoDArray, [[5, 6, 7, 8]], axis=0)

print(newTwoDArray)


def accessElements(array, rowIndex, colIndex):
    # len(array) returns number of rows
    # len(array[0]) returns number of columns
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])


# accessElements(newTwoDArray, 2, 3)


def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# traverse2DArray(newTwoDArray)


def search2DArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index ' + str(i) + " " + str(j)
    return 'The element is not found'


# print(search2DArray(newTwoDArray, 100))

# Deletion
newTDArray = np.delete(newTwoDArray, 2, axis=0)
print(newTDArray)
