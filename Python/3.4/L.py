import itertools

Arr = []

for i in range(int(input())):
    Arr.extend(input().split(', '))

Arr = sorted(list(Arr))

for i, j in enumerate(Arr, 1):
    print(str(i) + ". " + j)