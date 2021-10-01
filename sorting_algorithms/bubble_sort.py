# bubble sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j - 1]:
                buf = list[j - 1]
                list[j - 1] = list[j]
                list[j] = buf
    return list


def example_usage():
    list = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', list)
    print('Sorted:\t\t', bubble_sort(list))


if __name__ == "__main__":
    example_usage() # run an example on start