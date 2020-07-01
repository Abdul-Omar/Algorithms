def findMajority(numbers):
    if len(numbers) == 1:
        return numbers[0]

    mid = len(numbers) //2

    left = numbers[:mid]

    right = numbers[mid:]

    print("left is: ", left)
    print("right is : ", right)

    majority_left = findMajority(left)
    majority_right = findMajority(right)

    if isMajority(numbers,majority_left):
        return majority_left
    elif isMajority(numbers,majority_right):
        return majority_right

    return -1


def isMajority(numbers, value):
    return numbers.count(value) > (len(numbers) //2)
numbers = [1,1,1,3,7,8,5,1,1,1,4]
print(findMajority(numbers))
