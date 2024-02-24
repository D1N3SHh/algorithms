# convert the given decimal number into an equivalent binary number


def dec_to_bin(n):
    if n >= 1:
        dec_to_bin(n // 2)
    print( n % 2, end="")


def example_usage():
    binary = dec_to_bin(245)


if __name__ == "__main__":
    example_usage()