# heap sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


def max_heapify(A, i, heap_size):
    left = 2*i+1
    right = 2*i+2
    largest = i

    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right

    if largest != i:
        buf = A[i]
        A[i] = A[largest]
        A[largest] = buf
        max_heapify(A, largest, heap_size)


def bild_max_heap(A, heap_size):
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(A, i, heap_size)


def heap_sort(A):
    heap_size = len(A)
    bild_max_heap(A, heap_size)
    for i in range(heap_size - 1, 0, -1):
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
    example_usage() # run an example on start