# Using array module to create array
# It's a python standard library, no installation is required
# Advantage - It's more memory efficient than list for storing same type of data types
# Disadvantage - It doesn't support custom data type or mixed data types
import array

my_array = array.array('i')
# print(my_array)

my_array1 = array.array('i', [1, 2, 3, 4])
# print(my_array1)
my_array1.insert(4, 6)
# print(my_array1)


# Using Numpy array to create array
# import numpy as np
# np_array = np.array([], dtype=int)
# print(np_array)

# np_array1 = np.array([1,2,3,4])
# print(np_array1)

def traverseArray(array):
    for i in array:
        print(i)


# traverseArray(my_array1)


# Searching in array - We can use Liner Seach for arrays
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# print(linear_search(my_array1, 6))

# Delete an element from array
my_array1.remove(1)
print(my_array1)
