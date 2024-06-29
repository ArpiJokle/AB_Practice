def GCD(a, b):
    while a != b:
        if a > b:   
            a -= b
        else:
            b -= a
    return a


Arr = list(map(int, input().split(' ')))

if len(Arr) == 1:
    print(Arr[0])
    exit()

A = Arr[0]
B = Arr[1]
A = GCD(A, B)

for i in range(2, len(Arr)):
    A = GCD(A, Arr[i])

print(A)