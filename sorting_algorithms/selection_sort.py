# selection sort algorithm
# time complexity: O(n²)
# auxiliary space: O(1)


def selection_sort(A):
    for i in range(len(A) - 1):
        lowest = i
        for k in range(i + 1, len(A)):
            if A[k] < A[lowest]:
                lowest = k
        if lowest != i:
            A[lowest], A[i] = A[i], A[lowest]
    return A


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', selection_sort(A))


if __name__ == "__main__":
    example_usage()