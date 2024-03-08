# converts the given number (in any base from 2-9) to an equivalent decimal number
# time complexity: O(n)
# auxiliary space: O(1)


def any_to_dec(base, n):
    decimal = 0
    power = 1

    for i in range(len(n) - 1, -1, -1):
        decimal += int(n[i]) * power
        power = power * base

    return decimal


def example_usage():
    decimal = any_to_dec(2, "1101")
    print(decimal)


if __name__ == "__main__":
    example_usage()