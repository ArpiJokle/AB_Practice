n = int(input())

Sum = 0

for k in range(0, n):
    Str = input()
    flag = 0
    while Str != "�Ѩ":
        if Str == "�����":
            flag = 1
        Str = input()
    Sum += flag

print(Sum)