n = int(input())
maxDigit = 0
while n:
    if (n % 10) > maxDigit:
        maxDigit = n % 10
    n //= 10
print(maxDigit)
