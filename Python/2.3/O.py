n = int(input())

Count = 0

for i in range(0, n):
    Count += (input().find("�����") != -1)

print(Count)