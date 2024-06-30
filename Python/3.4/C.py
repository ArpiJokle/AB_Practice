import itertools

a, b, c = list(map(float, input().split()))

for i in itertools.count(a, c):
    if i <= b:
        print(i)
    else:
        break