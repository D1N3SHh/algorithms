# insertion sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


list = [3, 7, 1, 8, 4, 6, 9, 2, 5]


def insertion_sort(list):
    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        while i >= 0 and list[i] > key:
            list[i + 1] = list[i]
            i -= 1
        list[i + 1] = key


if __name__ == "__main__":
    insertion_sort(list)
    print(list)