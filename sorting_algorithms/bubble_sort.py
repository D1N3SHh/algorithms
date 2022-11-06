# bubble sort algorithm
# time complexity: O(n^2)
# auxiliary space: O(1)


def bubble_sort(A):
    n = len(A)
    swapped = False
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                swapped = True
                A[j - 1], A[j] = A[j], A[j - 1]
        if not swapped:
            break
    return A


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', bubble_sort(A))


if __name__ == "__main__":
    example_usage()