a = int(input())
b = int(input())

n = a
m = b

while n != m:
    if n > m:
        n -= m
    else:
        m -= n

print(int(a / n * b)) 