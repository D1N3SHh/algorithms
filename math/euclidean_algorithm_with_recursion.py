# finds greatest common divisor
# time complexity: O(log min(a,b))
# auxiliary space: O(log min(a,b))


def gcd(a, b):
    while a == 0:
        return b
    return gcd(b % a, a)


def example_usage():
    greatest = gcd(1122, 867)
    print(greatest)

if __name__ == "__main__":
    example_usage()