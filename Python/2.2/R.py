import math

a = int(input())
b = int(input())
c = int(input())

A = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
B = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
C = math.acos(((c ** 2) + (b ** 2) - (a ** 2)) / (2 * c * b))

if A < math.pi / 2 and B < math.pi / 2 and C < math.pi / 2:
    print("крайне мала")
    exit()

if A == math.pi / 2 or B == math.pi / 2 or C == math.pi / 2:
    print("100%")
    exit()

print("велика")