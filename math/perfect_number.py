# checks if the given number is perfect (perfect number is a positive integer that is equal to the sum of its positive divisors)


def is_perfect(n):
    divisors_sum = 0
    for i in range (1, n):
        if n % i == 0:
            divisors_sum += i

    if divisors_sum == n:
        return True
    else:
        return False


def example_usage():
    perfect = is_perfect(6) # True, because 1+2+3=6
    print(perfect)

if __name__ == "__main__":
    example_usage()