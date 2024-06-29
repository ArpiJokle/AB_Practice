def DigitSum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


N = int(input())

Name = input()
Max = DigitSum(int(input()))

for i in range(1, N):
    tempName = input()
    tempNum = DigitSum(int(input()))
    if tempNum >= Max:
        Max = tempNum
        Name = tempName

print(Name)