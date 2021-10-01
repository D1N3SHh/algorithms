# bubble sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


def bubble_sort(A):
    for i in range(0, len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j - 1], A[j] = A[j], A[j - 1]
    return A


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', bubble_sort(A))


if __name__ == "__main__":
    example_usage() # run an example on start