n = int(input())

i = 0
k = 0

while True:
    i += 1
    for j in range(1, i + 1):
        k += 1
        print(k, end=" ")
        if k == n:
            exit()
    print()