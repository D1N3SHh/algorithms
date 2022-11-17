# quick sort algorithm
# time complexity: O(n²) worst case | O(nlog n) average
# auxiliary space: O(n)


import random


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p ,r)


def randomized_quick_sort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q - 1)
        randomized_quick_sort(A, q + 1, r)
    return A


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    return A


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', quick_sort(A, 0, len(A) - 1))


if __name__ == "__main__":
    example_usage()