# quick sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


A = [3, 7, 1, 8, 4, 6, 9, 2, 5]


def partitions(A, p, r):
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
        q = partitions(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


if __name__ == "__main__":
    quick_sort(A, 0, len(A) - 1)
    print(A)