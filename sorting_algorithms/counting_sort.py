# counting sort algorithm (no negative numbers only)
# time complexity: θ(n+k) | θ(n) for k = O(n)
# auxiliary space: θ(n+k) | θ(n) for k = O(n)


def counting_sort(A):
    B = [0] * len(A)    # to store the sorted array
    k = max(A) + 1      # quantity of unique numbers
    C = []              # to count the number of successive numbers
    n = len(A)
    for i in range(0, k):
        C.append(0)
    for j in range(0, n):
        C[A[j]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for j in reversed(range(0, n)):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', counting_sort(A))


if __name__ == "__main__":
    example_usage()