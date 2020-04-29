data = [1, 3, 5, 7, 9, 11, 14, 15, 16, 19]
target = 15


# linear search algorithm
def linear_search(data, target):
    for i in range(len(data)):
        if target == data[i]:
            return True
    return False


# binary search recursive algorithm
def binary_recursive(data, target, min, max):
    if min > max:
        return False
    else:
        mid = (min + max) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_recursive(data, target, min, mid - 1)
        else:
            return binary_recursive(data, target, mid + 1, max)


# binary search iterative algorithm
def binary_search(data, target):
    min = 0
    max = len(data) - 1

    while min <= max:
        mid = (min + max) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            max = mid - 1
        else:
            min = mid + 1
    return False
