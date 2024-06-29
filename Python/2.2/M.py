Num = int(input())

a1 = Num % 10
a2 = int(Num / 10)

Num = int(input())

b1 = Num % 10
b2 = int(Num / 10)

Num = int(input())

c1 = Num % 10
c2 = int(Num / 10)

if a1 == b1 and b1 == c1:
    print(a1)
else:
    print(a2)