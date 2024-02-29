# searches for the index of an element in an already sorted array
# time complexity: O(log n)
# auxiliary space: O(log n)


def binary_search(A, left, right, x):
    if left <= right :
        middle = (left + right) // 2
        if A[middle] == x:
            return middle
        elif A[middle] < x:
            return binary_search(A, middle + 1, right, x)
        elif A[middle] > x:
            return binary_search(A, left, middle - 1, x)
    else:
        return "None"


def example_usage():
    A = [1, 2, 4, 5, 8, 9, 13, 16, 20]
    print('Index of "16":', binary_search(A, 0, len(A) - 1, 16))


if __name__ == "__main__":
    example_usage()