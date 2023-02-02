# finds max subarray
# time complexity: O(n)
# auxiliary space: O(1)


def max_crossing_subarray(list, low, mid, high):
    left_sum = -2147483647
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + list[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    right_sum = -2147483647
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + list[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def max_subarray(list, low, high):
    if low == high:
        return low, high, list[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray(list, low, mid)
        right_low, right_high, right_sum = max_subarray(list, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(list, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def example_usage():
    list = [3, -7, -1, 8, -4, 6, 9, -2, 5]
    low, high, sum = max_subarray(list, 0, len(list) - 1)
    print('Max subarray:', sum)
    print('Start index:', low)      # indexing from 0
    print('End index:', high)


if __name__ == "__main__":
    example_usage()