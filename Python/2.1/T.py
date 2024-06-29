N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

M1 = -int(N * (M - K1) / (K1 - K2))
print(N - M1, M1, sep=" ")