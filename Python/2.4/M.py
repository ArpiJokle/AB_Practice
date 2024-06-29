n = int(input())
m = int(input())

k = 0

Len = len(str(n * m))

for i in range(0, n):
    k = i + 1
    for j in range(0, m):
        print(str(k).rjust(Len), end=" ")
        k += n
    print()