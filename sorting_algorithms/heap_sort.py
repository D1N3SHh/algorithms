# heap sort algorithm
# time complexity: θ(nlog n)
# auxiliary space: θ(1)


def max_heapify(A, i, n):
    left = 2*i+1
    right = 2*i+2
    largest = i

    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right

    if largest != i:
        buf = A[i]
        A[i] = A[largest]
        A[largest] = buf
        max_heapify(A, largest, n)


def bild_max_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, i, n)


def heap_sort(A):
    n = len(A)
    bild_max_heap(A)
    for i in range(n - 1, 0, -1):
        buf = A[0]
        A[0] = A[i]
        A[i] = buf
        max_heapify(A, 0, i)
    return A


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', heap_sort(A))


if __name__ == "__main__":
    example_usage()