from sys import stdin

Lines = [x.strip().split() for x in stdin]

Arr = []

for i in Lines:
    Arr.extend(i)

Arr = sorted(list(set(Arr)))

for i in Arr:
    if i.lower() == i.lower()[::-1]:
        print(i)