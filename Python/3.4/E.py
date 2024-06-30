import itertools

Arr = input().split(', ')
Arr.extend(input().split(', '))
Arr.extend(input().split(', '))

Arr = sorted(list(set(Arr)))

for i, j in enumerate(Arr, 1):
    print(str(i) + ". " + j)