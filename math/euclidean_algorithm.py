# find greatest common divisor
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


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
    example_usage() # run an example on start