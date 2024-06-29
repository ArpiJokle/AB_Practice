import math


def Prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


N = int(input())

Count = 0

for i in range(0, N):
    Count += Prime(int(input()))

print(Count)