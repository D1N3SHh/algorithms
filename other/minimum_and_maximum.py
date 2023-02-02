# finding minimum and maximum
# time complexity: O(n)
# auxiliary space: O(1)


def minimum(A):
    min = A[0]
    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]
    return min


def maximum(A):
    max = A[0]
    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]
    return max

def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print("Minimum: ", minimum(A))
    print("Maximum: ", maximum(A))


if __name__ == "__main__":
    example_usage()