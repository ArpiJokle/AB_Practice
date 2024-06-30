import itertools
n = int(input())

A = list(range(1, n + 1))

A = list(itertools.product(A, A))

for i in range(0, n ** 2):
    print(A[i][0] * A[i][1], end=' ')
    if (i + 1) % n == 0:
        print()