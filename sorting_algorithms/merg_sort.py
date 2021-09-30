# merg sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


list = [3, 7, 1, 8, 4, 6, 9, 2, 5]


def merge(list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(0, n1):
        left[i] = list[p + i]
    for j in range(0, n2):
        right[j] = list[q + j + 1]
    left[n1] = 2147483647           # guard cards
    right[n2] = 2147483647          #
    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j = j + 1


def merge_sort(list, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(list, p, q)
        merge_sort(list, q + 1, r)
        merge(list, p, q, r)


if __name__ == "__main__":
    merge_sort(list, 0, len(list) - 1)
    print(list)