n = int(input())
m = int(input())

k = 0

Len = len(str(n * m))

for i in range(0, n):
    for j in range(0, m):
        k += 1
        print(str(k).rjust(Len), end=" ")
    print()