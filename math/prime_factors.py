# prints all prime factors of a given number
# time complexity: O(sqrt(n))
# auxiliary space: O(1)


def prime_factors(n):
    # check for even numbers (must be 2)
    while n > 1 and n % 2 == 0:
        print('2')
        n = n / 2

    # check for odd numbers
    factor = 3
    while n > 1:
        if n % factor == 0:
            print(factor)
            n = n / factor
        else:
            factor += 2


def example_usage():
    prime_factors(100) # 2 2 5 5

if __name__ == "__main__":
    example_usage()