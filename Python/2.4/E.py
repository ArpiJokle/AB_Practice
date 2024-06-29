n = int(input())

Sum = 0

for k in range(0, n):
    Str = input()
    flag = 0
    while Str != "ВСЁ":
        if Str == "зайка":
            flag = 1
        Str = input()
    Sum += flag

print(Sum)