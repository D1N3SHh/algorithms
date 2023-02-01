# finds greatest common divisor
# time complexity: O(log min(a,b))
# auxiliary space: O(log min(a,b))


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a

def example_usage():
    greatest = gcd(1122, 867)
    print(greatest)

if __name__ == "__main__":
    example_usage()