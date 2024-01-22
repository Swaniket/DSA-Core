# Write a function to find the missing number in a given integer array 1 to 100
# missing_number([1, 2, 3, 4, 6], 6) // OP -> 5

def missing_number(arr, n):
    sumOfNNaturalNumbers = n * (n+1) // 2
    arrTotal = sum(arr)
    return sumOfNNaturalNumbers - arrTotal


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    print(missing_number(arr, 6))
