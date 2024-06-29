n = int(input())

Count = 0

for i in range(0, n):
    Count += (input().find("зайка") != -1)

print(Count)