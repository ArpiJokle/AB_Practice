N = int(input())

if N == 0:
    print(1)
    exit()

Ans = 1

for i in range(1, N + 1):
    Ans *= i

print(Ans)