# finds greatest common divisor
# time complexity: O(log min(a,b))
# auxiliary space: O(log min(a,b))


def gcd(a, b):
    while a != 0 and b !=0:
        if a > b:
            a = a % b
        elif a < b:
            b = b % a
    if a == 0:
        return b
    elif b == 0:
        return a


def example_usage():
    greatest = gcd(1122, 867)
    print(greatest)

if __name__ == "__main__":
    example_usage()