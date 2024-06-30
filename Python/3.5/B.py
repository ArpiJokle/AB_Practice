from sys import stdin

Arr = stdin.readlines()

Sum = 0

for i in Arr:
    Sum += int(i.split()[2]) - int(i.split()[1])

print(round(Sum / len(Arr)))