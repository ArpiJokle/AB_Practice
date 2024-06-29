def GCD(a, b):
    while a != b:
        if a > b:   
            a -= b
        else:
            b -= a
    return a


n = int(input())

if n == 1:
    print(input())

a = int(input())
b = int(input())

a = GCD(a, b)

for i in range(0, n - 2):
    b = int(input())
    a = GCD(a, b)

print(a)