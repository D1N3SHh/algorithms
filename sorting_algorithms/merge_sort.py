# merg sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(0, n1):
        left[i] = A[p + i]
    for j in range(0, n2):
        right[j] = A[q + j + 1]
    left[n1] = 2147483647           # guard cards
    right[n2] = 2147483647          #
    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j = j + 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', merge_sort(A, 0, len(A) - 1))


if __name__ == "__main__":
    example_usage() # run an example on start