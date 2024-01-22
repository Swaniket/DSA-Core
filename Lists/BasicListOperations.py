# Content
# --------------------------------------
# Indexing, Modifying elements
# List methods .insert() .append() .extend()
# Slicing
# .pop(), .remove(), .delete()
# Searching
# --------------------------------------

shoppingList = ['Milk', 'Cheese', 'Butter']

# Access the first and last elemenet
# print(shoppingList[0], shoppingList[-1])

# Check if anything exists in the list
# print('Milk' in shoppingList)
# print('Bread' in shoppingList)

# Modify List elements
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    # print(shoppingList[i])

# print(shoppingList)

myList = [1, 2, 3, 4, 5, 6, 7]
# print(myList)
myList[2] = 33
print(myList)

# List Methods .insert() .append() .extend()
myList.insert(4, 45)
myList.append(55)
myList.extend(shoppingList)
# print(myList)

# Slicing
print(myList[0:2])  # First 2 elements of list
print(myList[1:])  # Prints all elements from the 2nd element
# Update first 2 elements in the list
myList[0:2] = ['x', 'y']
# print(myList)

# Deletion using .pop(), .delete(), .remove()
# .pop() returns the deleted elements
myList.pop()  # Delete the last element
myList.pop(1)  # second element will be deleted

# del doesn't return anything
del myList[0:2]

# We need to pass the specific element we deletee
myList.remove(45)

# print(myList)


# Searching
my_list2 = [10, 20, 30, 40, 50, 60, 70, 80]

# Method 1 - in operator
target = 500

if target in my_list2:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

# Method 2 - Linear Search


def linearSearch(p_list, target):
    for i, value in enumerate(p_list):
        if value == target:
            return i
    return -1


print(linearSearch(my_list2, 500))
