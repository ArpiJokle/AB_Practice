N = int(input())

Count = 0

for i in range(0, N):
    Str = input()
    Count += (Str == Str[::-1])

print(Count)