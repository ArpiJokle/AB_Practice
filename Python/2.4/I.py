def MaxNum(n):
    maxDigit = 0
    while n:
        if (n % 10) > maxDigit:
            maxDigit = n % 10
        n //= 10
    return maxDigit


N = int(input())

for i in range(0, N):
    print(MaxNum(int(input())), end="")