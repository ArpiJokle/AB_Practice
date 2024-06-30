N = int(input())
M = int(input())
Arr = []
for i in range(N + M):
    Arr.append(input())
Count = 0
for i in Arr:
    Count += int(Arr.count(i) == 1)
print(Count if Count != 0 else "Таких нет")