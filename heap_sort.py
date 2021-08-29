# heap sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


list = [3, 7, 1, 8, 4, 6, 9, 2, 5]


def max_heapify(list, i, heap_size):
    left = 2*i+1
    right = 2*i+2
    largest = i

    if left < heap_size and list[left] > list[largest]:
        largest = left
    if right < heap_size and list[right] > list[largest]:
        largest = right

    if largest != i:
        buf = list[i]
        list[i] = list[largest]
        list[largest] = buf
        max_heapify(list, largest, heap_size)


def bild_max_heap(list, heap_size):
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(list, i, heap_size)


def heap_sort(list):
    heap_size = len(list)
    bild_max_heap(list, heap_size)
    for i in range(heap_size - 1, 0, -1):
        buf = list[0]
        list[0] = list[i]
        list[i] = buf
        max_heapify(list, 0, i)


if __name__ == "__main__":
    heap_sort(list)
    print(list)