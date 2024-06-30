import itertools

Arr = []

for i in range(int(input())):
    Arr.extend(input().split(', '))

Arr = sorted(list(Arr))

for i in sorted(itertools.permutations(Arr, 3)):
    print(' '.join(i))