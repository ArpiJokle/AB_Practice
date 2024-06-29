import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
            exit()
        else:
            print("No solution")
            exit()
    print(-(c / b))
    exit()

if a != 0 and b == c and b == 0:
    print(0)
    exit()

D = b ** 2 - (4 * a * c)

if D < 0:
    print("No solution")
    exit()

if D == 0:
    print(f"{(-1 * b) / (2 * a):.2f}")
    exit()

A = (-1 * b - math.sqrt(D)) / (2 * a)
B = (-1 * b + math.sqrt(D)) / (2 * a)
if A < B:
    print(f"{A:.2f}", end=" ")
    print(f"{B:.2f}")
    exit()

print(f"{B:.2f}", end=" ")
print(f"{A:.2f}")