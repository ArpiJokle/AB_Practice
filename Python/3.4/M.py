import itertools

Arr = []

for i in range(int(input())):
    Arr.append(input())

for i in sorted(itertools.permutations(Arr, len(Arr))):
    print(', '.join(i))