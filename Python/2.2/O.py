Num1 = input()
Num2 = input()

Str = Num1 + Num2

Str = sorted(Str)[::-1]

Sum = 0

for i in range(1, len(Str) - 1):
    Sum += int(Str[i])

print(Str[0] + str(Sum % 10) + Str[len(Str) - 1])