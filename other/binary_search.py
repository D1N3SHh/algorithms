# searches for the index of an element in an already sorted array
# time complexity: O(log n)
# auxiliary space: O(1)


def binary_search(A, x):
    left = 0
    right = len(A) - 1

    while left <= right:
        middle = (left + right) // 2
        if A[middle] < x:
            left = middle + 1
        elif A[middle] > x:
            right = middle - 1
        else:
            return middle
    
    # the element was not present
    return "None"



def example_usage():
    A = [1, 2, 4, 5, 8, 9, 13, 16, 20]
    print('Index of "16":', binary_search(A, 16))


if __name__ == "__main__":
    example_usage()