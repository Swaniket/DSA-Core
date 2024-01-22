# This concept is unique for only Python

prev_list = [1, 2, 3]

# Lets consider this block of code
# It takes the previous list and multiplies 2 with every element and creates a new list
new_list = []
for i in prev_list:
    new_list.append(i*2)

# We can use this short hand by using list comprehension
new_list2 = [i*2 for i in prev_list]

# Lets look at another expression
language = "Python"
new_list3 = [letter for letter in language]
print(new_list3)  # ['P', 'y', 't', 'h', 'o', 'n']

# Conditional List Comprehension
# Lets look at this example where we only want to create a list with the possitive numbers
prev_list1 = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list4 = [number for number in prev_list1 if number > 0]
print(new_list4)

# Take only the square of the negetive numbers
new_list5 = [number*number for number in prev_list1 if number < 0]
print(new_list5)


# More complex example
# Lets write a program to filterout the consonants from a sentence
sentence = 'My name is Swaniket'


def is_consonanat(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels


consonanats = [i for i in sentence if is_consonanat(i)]
print(consonanats)


# We can also use an else case
# Lets use the prev example, and put 0 for all the -ve numbers
new_list6 = [number if number > 0 else 0 for number in prev_list1]
print(new_list6)
