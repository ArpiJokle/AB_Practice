def DigitSum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


n = int(input())

sum = 0

for i in range(0, n):
    sum += DigitSum(int(input()))

print(sum)