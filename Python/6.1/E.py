import math
A = tuple(map(float, input().split()))
B = tuple(map(float, input().split()))

C = (B[0] * math.cos(B[1]), B[0] * math.sin(B[1]))

print(math.sqrt((A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2))