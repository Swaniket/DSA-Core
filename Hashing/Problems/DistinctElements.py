# Given a list, count the distinct elements from the list
# [10,20,10,30,30,20] -> O/P = 3

def countDistinct1(lst):
    res = 1
    for i in range(1, len(lst)):
        if lst[i] not in lst[0: i]:
            res = res + 1
    return res


def countDistinct2(lst):
    return len(set(lst))


def countDistinct3(lst):
    uniqueElements = []

    for i in lst:
        if i not in uniqueElements:
            uniqueElements.append(i)

    return len(uniqueElements)


if __name__ == "__main__":
    lst = [10, 20, 10, 30, 30, 20]

    print(countDistinct1(lst))
    print(countDistinct2(lst))
    print(countDistinct3(lst))
