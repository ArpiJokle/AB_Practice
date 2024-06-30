import itertools

Arr = []
for i in range(int(input())):
    Arr.append(input())

for i, j in itertools.combinations(Arr, 2):
    print(i + " - " + j)