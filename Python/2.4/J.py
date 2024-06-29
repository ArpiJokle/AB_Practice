N = int(input())

print("À Á Â")

for i in range(1, N):
    for j in range(1, N - i):
        k = N - i - j
        if k > 0:
            print(i, j, k, sep=" ")