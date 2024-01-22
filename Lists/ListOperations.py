# Contains
# --------------------------------------
# List Operations / functions
# Operations - '+' operator and '* operators'
# Functions - len(), max(), min(), sum()
# Converting String to list
# Converting List to String
# Copy a list so that it won't modify the original list

# Operators
# '+' Operator
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)

# '*' Operator
d = [0]
e = a * 4
# print(e)


# Functions
list1 = [6, 1, 2, 4, 3, 5, 0]
print('Length is', len(list1))
print('Max element is', max(list1))
print('Min element is', min(list1))
print('Summation of elements', sum(list1))

# myList = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     myList.append(value)

# avg = sum(myList)/len(myList)
# print("Avg is", avg)

# Converting String to list
myString = 'spam'
list2 = list(myString)
print(list2)

myString2 = 'Hi my name is swaniket'
list3 = myString2.split()
print(list3)

myString3 = 'spam1-spam2-spam3'
delimiter = '-'
list4 = myString3.split(delimiter)
print(list4)


# Converting List to String
print(delimiter.join(list4))


# Copy a list so that it won't modify the original list
copyList1 = list1[:]
copyList1.sort()
print(copyList1)
print(list1)


# Lists vs Array --------------------------------------------
# Similarities
# 1. Both data structures are mutable.
# 2. Both can be indexed and iterated through.
# 3. They can be both sliced.

# Differences
# 1. Arrays are optimized for arthmatic operations
# 2. For lists the element types can be different, but for array, the types must be same.
