import itertools

Arr = []

for i in range(int(input())):
    Arr.append(input())

for i in sorted(itertools.permutations(Arr, 3)):
    print(', '.join(i))